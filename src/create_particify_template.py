#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__      = "Rico Hengst"
__contact__     = "rico.hengst@tropos.de"
__copyright__   = "TROPOS"
__date__        = "2025/12/01"
__deprecated__  = False
__email__       = "rico.hengst@tropos.de"
__license__     = "GPLv3"
__version__     = "0.0.1"


import os
import glob
from datetime import datetime
from jinja2 import Template
import re
import xlwt
import string



# dir of script
exec_dir = os.path.dirname(__file__)

# define 
particify_template  = exec_dir + "/template/particify_template.j2"
particify_out       = exec_dir + "/../html/particify_" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".csv"
raw_image_dir       = exec_dir + "/../images/"
reveal_template     = exec_dir + "/template/reveal.js_template.j2"
reveal_out          = exec_dir + "/../revealjs.html"



def scan_imagedir(raw_image_dir):
    
    print("Scan image dir: " + raw_image_dir)
    
    # get image files
    if not os.path.exists(raw_image_dir):
       print("The file not exists." + raw_image_dir)
       exit()
       

    dir_contents = os.listdir(raw_image_dir)
    if len(dir_contents) < 3:
        print("No images or dirs")
        exit()
        
    images = []
    for dir_content in dir_contents:
        if os.path.isfile(raw_image_dir + dir_content):
            basename_without_ext = os.path.splitext(os.path.basename(dir_content))[0]

            
            images.append( { "file_name" : dir_content, "name" : basename_without_ext.replace("_", " ") } )
        else:
            print("Not a file: " + raw_image_dir + dir_content)
            
        if len(images) < 1:
            print("No images")
            exit()
            
            
    # sort
    images = sorted(images, key=lambda d: d['name'])
    print(images)
    return images
        
    

def render_particify(images,particify_template, particify_out):
    
    print("Render template: " + os.path.basename(particify_template) )

    #winterurlaub2011.misc@vodafonemail.de
    #12ee!!KK
    #https://ttl255.com/jinja2-tutorial-part-3-whitespace-control/


    if not os.path.exists(particify_template):
       print("The file not exists." + particify_template)
       exit()
    
    current_dateTime = datetime.now()
    print(current_dateTime)

    context = {
        "images": images
    }


    # Create one external form_template html page and read it
    File = open(particify_template, 'r')
    content = File.read()
    File.close()

    # Render the template and pass the variables
    template = Template(content)
    rendered_form = template.render(context)

    # removed trailed new line after ...> ",,false,true,0
    #print(rendered_form)
    #rendered_form = rendered_form.replace('\\n\",,false,true,0', '\",,false,true,0')
    rendered_form = re.sub(r"\n\",,false,true,0", "\",,false,true,0", rendered_form)


    # save the txt file in the form.html
    output = open(particify_out, 'w')
    output.write(rendered_form)
    output.close()


def write_xls(images):

    style0 = xlwt.easyxf('font: name Arial, color-index blue, bold on',num_format_str='#,##0.00')
    stylebold = xlwt.easyxf('font: name Arial, bold on')
    style1 = xlwt.easyxf(num_format_str='YYYY-MM-DD HH:MM:SS')

    wb = xlwt.Workbook()
    ws = wb.add_sheet('CC @TROPOS Results')

    ws.write(0, 0, "Voting results", stylebold)
    ws.write(1, 0, datetime.now(), style1)


    yaxis_ofsetter = 3
    xaxis_ofsetter = 1
    n_questions    = 10
    
    # header
    alphabet = list(string.ascii_uppercase)
    for index_question in range(0, n_questions):
        ix = xaxis_ofsetter + index_question
        ws.write(yaxis_ofsetter -1, ix, "Question " + str(ix))
    ws.write(yaxis_ofsetter -1, n_questions + 2, "Sum", stylebold)
    ws.write(yaxis_ofsetter -1, n_questions + 4, "Image")
    
    # iterate vertical via cookies
    for index_image, image in enumerate(images):
        iy = yaxis_ofsetter + index_image
        
        ws.write(iy, 0, image["name"])
        ws.write(iy, xaxis_ofsetter + n_questions + 3, image["file_name"])
        # iterate horizontal via questions
        #print(index_image, image["name"])
        for index_question in range(0, n_questions):
            ix = xaxis_ofsetter + index_question
            
            # write 0 to each vote
            #ws.write(iy, ix, 4)
            
        # sum
        my_func = "SUM(" + alphabet[1] + str(iy+1) + ":" + alphabet[n_questions] + str(iy+1) + ")"
        ws.write(iy, n_questions + 2, xlwt.Formula(my_func),stylebold)
    
    xls_filename = "voting_evaluation.xls"
    user_input = input("Do you want to overide existing voting evaluation file \"" + xls_filename + "\"? (yes/no): ")
    if user_input.lower() in ["yes", "y"]:
        print("Continuing...")
        
        print( "Generate evaluation template: " + xls_filename)
        wb.save(xls_filename)
    else:
        print("Exiting...")
    

images = scan_imagedir(raw_image_dir)
render_particify(images,particify_template, particify_out)
render_particify(images,reveal_template, reveal_out)
write_xls(images)
