#Laravel Copy Helper#


A Python script to help copy and replace one laravel project with another while passing the necessary parameters via ***command line*** of the required files and folder to copy and overwrite in the other laravel project. Tested on Python 2.7, works on both Windows and Linux operating system.



Example
---------

 **Note:**
The script should be run from cmd line interface. And, it works on files in the root directory
of the laravel project.


    
    > python laravelcopy.py -h
    [+] laravelcopy.py -i <from_dir> -o <to_dir> -r <[folders_list]> -g <[files_list]>
	[+] laravelcopy.py -i <from_dir> -o <to_dir> --folders=<[folders_list]> 
		--files=<[files_list]>

    > python laravelcopy.py -i /var/www/mylaravelsite -o /var/www/laravel -r 
    ["app","database","routes"] -g [".env"]
	[-] Deleting /var/www/laravel/.env
	[+] Coping /var/www/mylaravelsite/.env
	[-] Deleting /var/www/laravel/app
	[+] Coping /var/www/mylaravelsite/app
	[-] Deleting /var/www/laravel/database
	[+] Coping /var/www/mylaravelsite/database
	[-] Deleting /var/www/laravel/routes
	[+] Coping /var/www/mylaravelsite/routes
	[+] Done!
	>
	> 

###License

This "Software" is Licensed Under  **`MIT License (MIT)`** .
        
        