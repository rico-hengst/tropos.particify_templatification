# tropos.particify_templatification

* jinja2 white space control: https://ttl255.com/jinja2-tutorial-part-3-whitespace-control/

## Pad
https://pad.gwdg.de/6rRk_P3HRk2HYaB7ZNEaSw#

## Umfrage
* zB https://ars.particify.de/p/07459025
* credentials zur Bearbeitung der Umfrage im Script


## Lokale Slideshow Cookies
* revealjs.html

## Onboarding Cookies
* alle jpg Bilder in Ordner "images" ablegen
* nur ein Bild pro Cookie
* Dateiname = Name die Cookies
* White Space in Dateiname ok
* Bilddatei im Querformat 3:2 oder 1:1, größte Seitenlänge 1550px
* Bildbearbeitung via gimp

## Slideshow und Umfragetemplate
* script src/create_particify_template.py ausführen
* Slidshow revealjs.html wird neu geschrieben, ggfalls Brwoserrefresh
* Umfragetemplate wird in /html/particify_<>.csv geschrieben
* Neue Umfrage erstellen:
    * erstellen einer neuen Umfrage ... Survey klicken https://ars.particify.de/edit/07459025
    * Name der Umfrage eingeben
    * vertikale Punkte, Import Contents -> Umfragetemplate hochladen
