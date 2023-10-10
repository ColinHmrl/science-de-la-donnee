from datetime import datetime
import os
from contextlib import redirect_stdout

def create_training_data(weight_path, model, model_name, num_classes, image_h, image_w, batch_size):
    # timestamp de debut
    folder = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    path = weight_path+folder
    # datetime object containing current date and time
    folder = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    if not os.path.exists(path):
        os.makedirs(path)

    # get model type
    if num_classes == 2:
        model_type = "binary"
    else:
        model_type = "multi"

    # readme 
    content = f"""# Training n°{folder}
    number of classes: {num_classes}
    model: {model_name}
    model type: {model_type}
    image size: {image_h}x{image_w}
    batch size: {batch_size}
    ----------------------------
    ## Compile config
    {model.get_compile_config()}
    ----------------------------
    ## Summary
    """

    file_path = os.path.join(path, "README.txt")

    # Write the string to the text file
    with open(file_path, "w") as text_file:
        text_file.write(content)
        with redirect_stdout(text_file):
            model.summary()

    return path