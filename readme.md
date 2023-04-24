# WordPress Search and Replace script

The script is specifically made for Linux servers and it requires WP-CLI and Python. 


# Table of contents
* [Calling/Executing the script](#Calling/Executing)
* [Technologies](#Technologies)
* [Contibuting](#Contributing)
* [License](#License)


## Calling/Executing

1. If the script is called locally, make sure to comment line 88:
    - os.system("rm -f sandr.py") - Removes script after it is executed.
2. If the script is called remotely, you would most likely want to delete it after use so line 88 can stay:
```bash 
wget -q https://github.com/LilkoPetkov/WordPress-Search-Replace; python3 search_replace.py
```
3. The script will:
    - Ask you if you wish to create a database backup before initiating the search and replace
    - Show the size of the website's folder and if you wish to create a backup for it. 
    - Ask for a URL to search 
    - Ask for a URL to replace
    - Ask if you wish to replace the entries in the .css files as well
    - Flush all caching
    
## Technologies
 
 - Python 3.9 / 3.11
 - WP-CLI 2.7.1


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.


## License

[MIT](https://choosealicense.com/licenses/mit/)
