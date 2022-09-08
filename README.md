# Creating BibTeX bibliographies for LaTeX with Zotero

1) Download the scripts, which export BibTeX bibliographies. They are the js-files in the following github https://github.com/vladislavivanistsev/zotero-bibtex 

2) Go to Zotero Tools > Preferences > Advanced > Files and Folders > Show Data Directory. A window will open. Navigate to the translators folder and copy the js-files there.

3) Restart Zotero.

4) Go to Zotero Tools > Preferences > Export and choose BibTeX-cite-UC in the Default Output Format drop-down menu.

# Exporting a bib-file

1) All the articles that are to be cited should have a mutual tag in Zotero. Tags can be added by highlighting the item, selecting Tags in the menu on the right, clicking Add and either naming the tag appropriately or choosing an existing tag.

2) The bibliography is created by choosing the desired tag from the bottom left menu, highlighting the items, then Right-Click > Export Items … > Format: BibTeX-export-UC. Tick Use Journal Abbreviation, untick other options and save the bibliography.

3) The resulting bib-file is to be defined in LaTeX to be recognized as the bibliography.

# About the universal citekey

https://github.com/cparnot/universal-citekey-js

# Adding references to LaTeX

1) To copy a citation to LaTeX, the desired item needs to be highlighted in Zotero, and the key combination ctrl-shift-c pressed. 

2) The reference is inserted into LaTeX with ctrl-v.

# Some Zotero tricks

* Bibliographies can be merged and modified manually with any text editor.

* Bibliographies may have redundant entries but must have all entries that are cited in the text. 

* A useful trick is to assign a color to the tag in the bottom left menu. That enables the use of hotkeys (number keys derived from the tag placement) to add the tag to Zotero items.

* When citing multiple items, highlight all of them before pressing ctrl-shift-c.

# Journals for RSS

1. Export "Exported Items.ris" from Zotero to a directory

2. Run "python RSS.py" in that directory

3. Examine journals_counts.log and journal_names.log

4. Find up to 20 rss feed of the most relevant journals and combine them at feedmix.novaclic.com/

5. Filter the combined feed with regex or by a keyword at siftrss.com

6. Start reading the refined feed into your favorite RSS reader or Zotero
