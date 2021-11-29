import os

def list_all_files(directory):
  list_of_files = os.listdir(directory)

  array = []

  path = directory
  for (dirpath, dirnames, filenames) in os.walk(path):
      if ( not (dirpath == os.path.basename(directory)) and
      (os.path.isdir(dirpath))
      and not (os.path.basename(dirpath).startswith('__')) ):
        for file in filenames:
            list_path_name = dirpath.split('/')
            if not (file.startswith('.')):
                module = ".".join(list_path_name) + "." + os.path.splitext(file)[0]
                module = module.lstrip(".opt.weirdAAL.")
                array.append(module)
                
  return array
