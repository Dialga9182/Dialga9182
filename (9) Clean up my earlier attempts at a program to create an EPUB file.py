
import os
from zipfile import ZipFile

### Create Templates
text_in_mimetype_file = '''application/epub+zip
'''
text_in_container_XML = '''<?xml version='1.0' encoding='utf-8'?>
<container xmlns="urn:oasis:names:tc:opendocument:xmlns:container" version="1.0">
  <rootfiles>
    <rootfile media-type="application/oebps-package+xml" full-path="EPUB/content.opf"/>
  </rootfiles>
</container>
'''
text_in_main_css_file = '''@namespace epub "http://www.idpf.org/2007/ops";

body {
    font-family: Verdana, Helvetica, Arial, sans-serif;
}

h1 {
    text-align: center;
}

h2 {
    text-align: left;
    font-weight: bold;
}

ol {
    list-style-type: none;
    margin: 0;
}

ol > li {
    margin-top: 0.3em;
}

ol > li > span {
    font-weight: bold;
}

ol > li > ol {
    margin-left: 0.5em;
}

.spoiler {
    padding-left: 0.4em;
    border-left: 0.2em solid #c7ccd1;
}


'''
text_in_nav_css_file = '''BODY {color: white;}
'''
text_in_content_opf_file = '''<?xml version='1.0' encoding='utf-8'?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="id" version="3.0" prefix="rendition: http://www.idpf.org/vocab/rendition/#">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
    <meta property="dcterms:modified">2022-07-21T07:46:22Z</meta>
    <meta name="generator" content="Ebook-lib 0.17.1"/>
    <dc:identifier id="id">Gn7pcR89</dc:identifier>
    <dc:title>Epub Title</dc:title>
    <dc:language>en</dc:language>
    <dc:creator id="creator">Epub Author</dc:creator>
    <dc:description>&lt;p&gt;Sentence description.&lt;/p&gt;</dc:description>
  </metadata>
  <manifest>
    <item href="style/main.css" id="doc_style" media-type="text/css"/>
    <item href="style/nav.css" id="style_nav" media-type="text/css"/>
    <item href="introduction.xhtml" id="chapter_0" media-type="application/xhtml+xml"/>
    <item href="nav.xhtml" id="nav" media-type="application/xhtml+xml" properties="nav"/>
    <item href="chap_1.xhtml" id="chapter_1" media-type="application/xhtml+xml"/>
    <item href="toc.ncx" id="ncx" media-type="application/x-dtbncx+xml"/>
  </manifest>
  <spine toc="ncx">
    <itemref idref="chapter_0"/>
    <itemref idref="nav"/>
    <itemref idref="chapter_1"/>
  </spine>
</package>
'''
text_in_toc_ncx_file = '''<?xml version='1.0' encoding='utf-8'?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1" xml:lang="en">
  <head>
    <meta name="dtb:uid" content="Gn7pcR89"/>
    <meta name="dtb:depth" content="2"/>
    <meta name="dtb:generator" content="calibre (6.1.0)"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
  </head>
  <docTitle>
    <text>Epub Title</text>
  </docTitle>
  <navMap>
    <navPoint id="num_1" playOrder="1">
      <navLabel>
        <text>Introduction</text>
      </navLabel>
      <content src="introduction.xhtml"/>
    </navPoint>
    <navPoint id="num_2" playOrder="2">
      <navLabel>
        <text>Chapter 1 name</text>
      </navLabel>
      <content src="chap_1.xhtml"/>
    </navPoint>
  </navMap>
</ncx>

'''
xhtml_text_in_chap_1_xhtml_file = '''<?xml version='1.0' encoding='utf-8'?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" epub:prefix="z3998: http://www.daisy.org/z3998/2012/vocab/structure/#" lang="en" xml:lang="en">
  <head>
    <title>S Class Mission Revealed</title>
    <link href="style/main.css" rel="stylesheet" type="text/css"/>
  </head>
  <body><h2>S Class Mission Revealed</h2>hellohello hello</body>
</html>

'''
xhtml_text_in_introduction_xhtml_file = '''<?xml version='1.0' encoding='utf-8'?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" epub:prefix="z3998: http://www.daisy.org/z3998/2012/vocab/structure/#" lang="en" xml:lang="en">
  <head>
    <title>Introduction</title>
  </head>
  <body><h1>Spying no Jutsu</h1>


	<p>Original source:
		<a rel="noopener noreferrer" href="https://www.fanfiction.net/s/2859078/1/Spying-no-Jutsu">https://www.fanfiction.net/s/2859078/1/Spying-no-Jutsu</a></p>
	
</body>
</html>

'''
xhtml_text_in_nav_xhtml_file = '''<?xml version='1.0' encoding='utf-8'?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en" xml:lang="en">
  <head>
    <title>Spying no Jutsu</title>
    <link href="style/main.css" rel="stylesheet" type="text/css"/>
  </head>
  <body>
    <nav epub:type="toc" id="id" role="doc-toc">
  <h1>Spying no Jutsu</h1>
  <ol>
    <li><a href="introduction.xhtml">Introduction</a></li>
    <li><a href="chap_1.xhtml">S Class Mission Revealed</a></li>
  </ol>
</nav>
</body>
</html>
'''
### Create Templates


### Create A Bunch Of Folders
    # Creates a folder called Main_Folder in current working directory
current_directory = os.getcwd()
Main_Folder = os.path.join(current_directory,"Main Folder")
if not os.path.exists(Main_Folder):
    os.mkdir(Main_Folder)
    # Returns Main_Folder as a File Path

    # Creates a folder called META-INF in Main_Folder
META_INF_Folder = os.path.join(Main_Folder, "META-INF")
if not os.path.exists(META_INF_Folder):
    os.mkdir(META_INF_Folder)
    # Returns META_INF_Folder as a File Path

    # Creates a folder called EPUB in Main_Folder
EPUB = os.path.join(Main_Folder, "EPUB")
if not os.path.exists(EPUB):
    os.mkdir(EPUB)
    # Returns EPUB as a File Path

    # Creates a style folder in EPUB folder
style_folder = os.path.join(EPUB, "style")
if not os.path.exists(style_folder):
    os.mkdir(style_folder)
    # Returns style_folder as a File Path
### Create A Bunch Of Folders


### Create A Bunch Of Files & Use Templates To Write Into Them
    # Creates a mimetype file in Main_Folder and writes
    # in it the text_in_mimetype_file
mimetype_file = open(f"{Main_Folder}\\mimetype.","w+")
mimetype_file.write(f"{text_in_mimetype_file}")
mimetype_file.close()
    
    # Creates an xml container file in the META-INF folder and writes
    # in it the text_in_container_XML
container_dot_XML_file = open(f"{META_INF_Folder}\\container.xml","w+")
container_dot_XML_file.write(text_in_container_XML)
container_dot_XML_file.close()
    
    # Creates main.css in style_folder and writes
    # in it the text_in_main_css_file
main_CSS_File = open(f"{style_folder}\\main.css","w+")
main_CSS_File.write(text_in_main_css_file)
main_CSS_File.close()
    
    # Creates nav.css in style_folder and writes
    # in it the text_in_nav_css_file
nav_CSS_File = open(f"{style_folder}\\nav.css","w+")
nav_CSS_File.write(text_in_nav_css_file)
nav_CSS_File.close()
    
    # Creates toc.ncx in EPUB and writes
    # in it the text_in_toc_ncx_file
toc_NCX_File = open(f"{EPUB}\\toc.ncx","w+")
toc_NCX_File.write(text_in_toc_ncx_file)
toc_NCX_File.close()
    
    # Creates content.opf in EPUB and writes
    # in it the text_in_content_opf_file
content_OPF_File = open(f"{EPUB}\\content.opf","w+")
content_OPF_File.write(text_in_content_opf_file)
content_OPF_File.close()
    
    # Creates chap_1.xhtml in EPUB and writes
    # in it the xhtml_text_in_chap_1_xhtml_file
chap_1_XHTML_File = open(f"{EPUB}\\chap_1.xhtml","w+")
chap_1_XHTML_File.write(xhtml_text_in_chap_1_xhtml_file)
chap_1_XHTML_File.close()
    
    # Creates introduction.xhtml in EPUB and writes
    # in it the xhtml_text_in_introduction_xhtml_file
introduction_XHTML_File = open(f"{EPUB}\\introduction.xhtml","w+")
introduction_XHTML_File.write(xhtml_text_in_introduction_xhtml_file)
introduction_XHTML_File.close()
    
    # Creates nav.xhtml in EPUB and writes
    # in it the xhtml_text_in_nav_xhtml_file
nav_XHTML_File = open(f"{EPUB}\\nav.xhtml","w+")
nav_XHTML_File.write(xhtml_text_in_nav_xhtml_file)
nav_XHTML_File.close()
### Create A Bunch Of Files & Use Templates To Write Into Them


#zip_object = ZipFile("NeewEbook.zip","w")
#zip_object.write(f"{Main_Folder}\\EPUB")
#zip_object.write(f"{Main_Folder}\\META-INF")
#zip_object.write(f"{Main_Folder}\\mimetype.")
#zip_object.close()