# Creating BibTeX bibliographies for LaTeX with Zotero

1) Download the scripts, which export BibTeX bibliographies. They are the js-files in the following git hub https://github.com/vladislavivanistsev/zotero-bibtex 

2) Go to Zotero Tools > Preferences > Advanced > Files and Folders > Show Data Directory. A window will open. Navigate to the translators folder and copy the js-files there.

3) Restart Zotero.

4) Go to Zotero Tools > Preferences > Export and choose BibTeX-cite-UC in the Default Output Format dropdown menu.

# Exporting a bib-file

1) All the articles that are to be cited should have a mutual tag in Zotero. Tags can be added by highlighting the item, selecting Tags in the menu on the right, clicking Add and either naming the tag appropriately or choosing an existing tag.

2) The bibliography is created by choosing the desired tag from the bottom left menu, highlighting the items, then Right-Click > Export Items … > Format: BibTeX-MTS-UC. Tick Use Journal Abbreviation, untick other options and save the bibliography.

3) The resulting bib-file is to be defined in LaTeX to be recognized as the bibliography

# Adding references to LaTeX

1) To copy a citation to LaTeX, the desired item needs to be highlighted in Zotero and the key combination ctrl-shift-c pressed. 

2) The reference is inserted into LaTeX with ctrl-v.

# Some Zotero tricks
* Bibliographies can be merged and modified manually with any text redactor.
* Bibliographies may have redundant entries, but must have all entries that are cited in text. 
* A useful trick is to assign a color to the tag in the bottom left menu. That enables the use of hotkeys (number keys derived from the tag placement) to add the tag to Zotero items.
* When citing multiple items, highlight all of them before pressing ctrl-shift-c.
