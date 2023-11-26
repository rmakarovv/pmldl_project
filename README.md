# Disaster tweet Generation and Detection
This repository is contains source code and reports for the project on Practical ML and DL course.

        authors: Roman Makarov & Adela Krylova
        e-mails: o.makarov@innopolis.university & a.krylova@innopolis.university

## The project can be run in the following steps:

0. Clone github repository with `git clone https://github.com/rmakarovv/pmldl_project.git`
1. Run `!pip install requirements.txt`
2. Download and extract data for training and testing

        python make_dataset.py --data-url <custom_url> --output-path <custom_output_path> --extract-path <custom_extract_path>

    Note that you can set up custom dataset url, ouutput and extract pathes 

3. If you'd like to explore the data, go to `notebooks/1_0_initial_data_exploration.ipynb` and click `Run all`. The text boxes above code lines explain the procedure comprehensively.
4. Run `notebooks/2_0_run_training.ipynb` to train generator and discriminator
5. Run `notebooks/3_0_evaluate_generator.ipynb` to evaluate generator. This notebook:
    1) Trains DistilBERT for 2 epochs (one of the best results on Kaggle)
    2) Writes down all generated samples that fooled the resulting model to `data/final/tricked.txt` 
6. To evaluate discriminator submit `submission_end` file to Kaggle competition.

## The best results we obtained are:
1. Discriminator accuracy was improved from 57% (almost no training data) to 68% on competition validation dataset
2. Generator model was able to fool DistilBERT model in 68% of generated data! (DistilBERT has one of the best results on kaggle with 85% accuracy).