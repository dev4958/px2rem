# px2rem

Converts px to rem values in a specified file, given a root font size.

### Usage

`$python3 px2rem.py [file path] [root font size]`

Outputs the contents of the file at [file path] with px values converted to rem values inside the file "output.txt" found in the root directory of this project.  Ignores @media query lines leaving anything specified in px inside the same.

##### [file path]

Any file of any type (CSS, SASS, SCSS, et cetera).

##### [root font size]

The root font size, which all rem values are calculated relative to (integer or float value in px units).  No need to add the "px" suffix to the value, for example, "16" is fine, no need to specify "16px".

### Example

`$python3 px2rem.py ~/file.css 16`

Takes file.css and converts all the px values specified inside to rem values corresponding to a root font size of 16px.  So if there's a line in file.css with the value 16px it will be converted to 1.000rem, 8px would be converted to 0.500rem, and so on.
