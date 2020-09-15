![aaple](src/images/apple-768x512.png)

# APIS-PROJECT 
## (Apple shares value related to iPhone models introduction)

### Analysis program of the evolution of Apple's shares between 2010 and 2020 in relation to the launch of new iPhone models.
### 
## Using the program and available commands

####Run some of these commands in Terminal as follows. Two types of report are available.
##### - Report by user-defined period of time: 



- python3 main.py -h, --help  show this help message and exit
- python3 main.py  -m MAIL, --mail MAIL  Introduce your mail
- python3 main.py  -f DATEFROM, --dateFrom DATEFROM
                        Introduce the starting date for the analysis in format
                        YYYY-MM-DD. Please, note that data is only available
                        from 2010 so the input date must be equal or later
- python3 main.py  -t DATETO, --dateTo DATETO
                        Introduce the ending date for the analysis in format
                        YYYY-MM-DD. Please, note that data is only available
                        until september 2020 so the input date must be equal
                        or later
- python3 main.py  -l MODEL, --model MODEL
                        Introduce Iphone model. Available from iPhone 4 (2010)
                        to iPhone SE (2020). Input must be equal to: iphone 4
                        iPhone 4s iPhone 5 iPhone 5s iPhone 5c iPhone 6 iPhone
                        6 Plus iPhone 6s iPhone 6s Plus iPhone SE (1ª
                        generación) iPhone 7 iPhone 7 Plus iPhone 8 iPhone 8
                        Plus iPhone X iPhone XS iPhone XS Max iPhone XR iPhone
                        11 iPhone 11 Pro iPhone 11 Pro Max iPhone SE (2ª
                        generación)

###Root

	- Working_file.ipynb: Jupyter notebook to clean the dataset (internal use)
	- Visualizer.ipynb: Jupyter notebook to obtain specific data from the dataset
	- RastreAmazon.ipynb: Jupyter notebook containing the conclusions and the app.
	- app_moviles.py: for internal use in RastreAmazon.ipynb
	 
	- input folder:
		 + 20191226-items.csv: contains the list of phones by model and branch.
		 + 20191226-reviews.csv: contains the reviews for the phones in items.csv

	- output folder:
		 +itera.csv: internal use file resulting from cleaning in Working_file.ipynb
		 +images folder:
		 	+several images for internal use in RastreAmazon.ipynb
	- src: 
		 +funciones.py: for internal use in Working_file.ipynb and Visualizer.ipynb
	 

## 3. SOURCE
Dataset extracted from Kaggle: [Kaggle link to repo](https://www.google.com)https://www.kaggle.com/tarunpaparaju/apple-aapl-historical-stock-data/notebooks





### H3
#### H4
##### H5
###### H6
