from pathlib import Path
import re
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from PIL import Image
ROOT=Path(__file__).resolve().parents[1];ASSETS=ROOT/'dist/assets'
for name,file in [('Body','DejaVuSans.ttf'),('Strong','DejaVuSans-Bold.ttf')]:
 pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+file))
INK=HexColor('#172b26');MUTED=HexColor('#53645b');GREEN=HexColor('#224e40');PAPER=HexColor('#f6f7f2')
c=canvas.Canvas(str(ASSETS/'CV_Nathan_Rebourg.pdf'),pagesize=(595.28,841.89));c.setTitle('Nathan Rebourg - CV');c.setAuthor('Nathan Rebourg')
c.setFillColor(PAPER);c.rect(0,0,595.28,841.89,fill=1,stroke=0)
c.setFillColor(GREEN);c.rect(0,663,595.28,179,fill=1,stroke=0)
def text(x,y,t,size=9,color=INK,font='Body'):
 c.setFillColor(color);c.setFont(font,size);c.drawString(x,y,t)
def para(x,y,w,t,size=9,color=INK,leading=None):
 t=re.sub(r'&(?![a-zA-Z#0-9]+;)', '&amp;', t)
 style=ParagraphStyle('p',fontName='Body',fontSize=size,leading=leading or size*1.48,textColor=color)
 p=Paragraph(t,style);_,h=p.wrap(w,800);p.drawOn(c,x,y-h);return y-h
# Header: no claim of a specific job search.
text(28,795,'Nathan Rebourg',27,white,'Strong')
text(29,769,'Entrepreneur & créateur de contenu',12,white,'Strong')
para(29,746,395,'Développement et automatisation<br/>Réseaux & télécommunications',9,HexColor('#dce7dc'))
para(29,707,400,'Je développe une activité de création de contenu et des outils utiles au quotidien, en parallèle de mes études et de mon alternance chez Orange.',9,white)
im=Image.open(ASSETS/'portrait-480.webp');c.drawImage(ImageReader(im),468,688,width=97,height=129,mask='auto')
# Sidebar
c.setStrokeColor(HexColor('#d8ded5'));c.line(187,31,187,637)
def side(title,items,y):
 text(27,y,title,10,GREEN,'Strong');y-=19
 for item in items: y=para(27,y,143,item,8.4,MUTED,12.5)-7
 return y-17
y=635
y=side('Contact',['<link href="mailto:nathanreb69@gmail.com">nathanreb69@gmail.com</link>','06 74 24 80 73','Lyon / Roanne','Permis B'],y)
y=side('En ligne',['<link href="https://www.linkedin.com/in/nathan-rebourg-901783333">LinkedIn / Nathan Rebourg</link>','<link href="https://github.com/Nathanrebourg">GitHub / Nathanrebourg</link>','<link href="https://www.youtube.com/@AnymeRediffs">YouTube / Anyme Rediffs</link>','<link href="https://nathan-rebourg.greybead8193.chatgpt.site">Portfolio / projets et démos</link>'],y)
y=side('Compétences',['HTML, CSS, JavaScript','Python, Git et GitHub','Automatisation vidéo, FFmpeg','Docker, interfaces web','Montage et formats courts','Planification et coordination'],y)
y=side('Langues',['Anglais : niveau scolaire B1','Allemand : niveau scolaire B2'],y)
y=side('Centres d’intérêt',['Investissement, automobile','Sport, voyages','Musique, saxophone'],y)
# Main column
x=209;w=357;y=635
def section(title,y):
 text(x,y,title,12,GREEN,'Strong');return y-19
def entry(title,sub,body,y):
 y=para(x,y,w,title,9.8,INK,13.5)-3
 if sub: y=para(x,y,w,sub,8,MUTED,11)-5
 y=para(x,y,w,body,8.6,INK,12.3)-9
 return y
y=section('Entrepreneuriat et projets',y)
y=entry('Création de contenu | Anyme Rediffs','Activité entrepreneuriale','Sélection éditoriale, montage et diffusion de formats courts. Développement d’audience et organisation de la production en parallèle des études et de l’alternance.<br/><b>Environ 40 000 abonnés et plus de 5 000 € générés</b> par l’activité (repères d’octobre 2026).',y)
y=entry('NRclip','Python · FFmpeg · Docker · interface web','Détection de moments forts sur Twitch, génération de clips verticaux sous-titrés et revue sur téléphone. Une chaîne de traitement au service de mon activité de contenu.',y)
y=entry('Liaison','HTML, CSS, JavaScript · Python · macOS','Interface locale réunissant agenda Apple, projets, finances et rapports YouTube. Connexions aux services, suivi des synchronisations et sauvegardes locales.',y)
y=section('Expériences',y-8)
y=entry('Pilote d’activité client et entreprise','Orange, Lyon | Alternance depuis septembre 2025','Supervision depuis les bureaux de techniciens sur le terrain : mises en service, changements d’offre et SAV, principalement pour les entreprises. Planification, gestion des aléas et des événements Orange, vérifications et coordination entre clients, partenaires et collègues.',y)
y=entry('Vice-président du bureau des étudiants R&T','IUT de Roanne | Octobre 2024 - novembre 2025','Gestion du pôle événementiel et travail en équipe.',y)
y=entry('Préparateur automobile','Renault Thivolle, Mâcon | Juillet 2024','Préparation des véhicules, vérifications et respect des délais de livraison.',y)
y=section('Formation',y-8)
y=entry('BUT Réseaux & Télécommunications','UJM, IUT de Roanne | Depuis 2024','Parcours Réseaux Opérateurs et Multimédia.',y)
y=entry('Baccalauréat STI2D, spécialité SIN','Lycée Louis Armand, Villefranche-sur-Saône | 2024','',y)
assert y>17, y
c.save();print('CV: bas du contenu',round(y),'pt')
# Native layout for the social card. Rendered to PNG separately.
s=canvas.Canvas('/tmp/portfolio-social.pdf',pagesize=(1200,630));s.setFillColor(PAPER);s.rect(0,0,1200,630,fill=1,stroke=0)
s.setFillColor(GREEN);s.rect(808,0,392,630,fill=1,stroke=0)
s.drawImage(ImageReader(im),824,40,width=352,height=469,mask='auto')
s.setFillColor(GREEN);s.setFont('Strong',48);s.drawString(64,528,'nr.')
s.setFont('Strong',58);s.drawString(64,411,'Nathan Rebourg')
s.setFont('Body',30);s.drawString(67,344,'Des idées. Du code. Du concret.')
s.setStrokeColor(HexColor('#a35b36'));s.setLineWidth(4);s.line(68,288,148,288)
s.setFont('Body',23);s.setFillColor(MUTED);s.drawString(67,223,'Création de contenu · Automatisation')
s.drawString(67,183,'Projets personnels & entrepreneuriat')
s.setFont('Strong',19);s.setFillColor(GREEN);s.drawString(67,80,'PORTFOLIO');s.save()
