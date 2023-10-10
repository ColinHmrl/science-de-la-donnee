def check_images(dir_path):
    print('CHECK IMAGES:')
    sub_dirs = os.listdir(dir_path)
    for sub_dir_name in sub_dirs:
      sub_dir_path = os.path.join(dir_path, sub_dir_name)
      if not os.path.isdir(sub_dir_path): continue
      print("-",sub_dir_name.upper())
      for file_name in tqdm(os.listdir(sub_dir_path)):
          file_path = os.path.join(sub_dir_path, file_name)

          if os.path.isfile(file_path):
              # Check if the file is an image (you can add more image formats if needed)
              if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
                  try:
                      with Image.open(file_path) as img:
                       # if img.width < min_w or img.height < min_h:
                       #   raise Exception(f'Too small img of shape {img.width},{img.height}')
                        cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
                        img_bytes = tf.io.read_file(file_path)
                        tf.io.decode_image(img_bytes)
                        img.verify()
                  except Exception as e:
                      #os.remove(file_path)
                      print(f'\nDeleting {file_path} due to an error: {str(e)}')
              else:
                #os.remove(file_path)
                print(f'\nSkipped {file_path} due to bad type {file_name.lower()}')