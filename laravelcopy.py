#!/usr/bin/python

import shutil, os, sys, getopt

        
def main(argv):
    filename = os.path.basename(__file__)
    
    from_dir = ''
    to_dir = ''
    folders = []
    files = []

    try:
        opts, args = getopt.getopt(argv,"hi:o:r:g:",["idir=","odir=",
                                                 "folders=","files="])
    except getopt.GetoptError:        
        print "[+] " + filename + ' -i <from_dir> -o <to_dir> -r <[folders_list]> -g <[files_list]>'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print "[+] " + filename + ' -i <from_dir> -o <to_dir> -r <[folders_list]> -g <[files_list]>'
            sys.exit()
        elif opt in ("-i", "--idir"):
            from_dir = arg
        elif opt in ("-o", "--odir"):
            to_dir = arg
        elif opt in ("-r", "--folders"):
            folders = map(str, arg.strip('[]').split(','))
        elif opt in ("-g", "--files"):
            files = map(str, arg.strip('[]').split(','))

    # Test it is a dir
    if not (os.path.isdir(from_dir) and os.path.isdir(to_dir)):
        print "[-] Either <from_dir> or <to_dir> is not a valid directory path."
        sys.exit()

    # Test it is a laravel project
    if not (os.path.exists(os.path.join(from_dir, 'artisan'))
            and os.path.exists(os.path.join(to_dir, 'artisan'))):
        print "[-] Either <from_dir> or <to_dir> is not a valid laravel project base directory path."
        sys.exit()
        
    # Copy to destinations
    for item in os.listdir(from_dir):
        path = os.path.join(from_dir, item)
        if os.path.isfile(path):
            if item in files:
                _to_path = os.path.join(to_dir, item)
                print "[-] Deleting %s" % _to_path

                try:
                    os.remove(_to_path)
                except:
                    pass
                
                print "[+] Coping %s" % path
                shutil.copy(path, to_dir)
        else:
            if item in folders:
                _to_path = os.path.join(to_dir, item)
                print "[-] Deleting %s" % _to_path

                try:
                    shutil.rmtree(_to_path)
                except:
                    pass
                
                print "[+] Coping %s" % path
                shutil.copytree(path, _to_path)

    print "[+] Done!"
    

                
if __name__ == "__main__":
   main(sys.argv[1:])
   
