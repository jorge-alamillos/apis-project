
import sys
import argparse
import pandas as pd
import src.generate_plots as gp
import src.generate_pdf as pdf

#Función para validar el modelo introducido. No funciona (pdte.)
'''
def validaModel(modelo):
    if modelo:
        valid_models = ["iPhone 4","ihone 4s","iphone 5",
                    "iphone 5s","iphone 5c","iphone 6",
                    "iphone 6 plus","iphone 6s","iphone 6s plus",
                    "iphone SE (1ª generación)","iphone 7","iphone 7 plus",
                    "iphone 8","iphone 8 plus","iphone X","iphone XS",
                    "iphone XS Max","iphone XR","iphone 11","iphone 11 pro",
                    "iphone 11 pro Max","iphone SE (2ª generación)" ]
        if modelo in valid_models:
            return modelo
        else:
            error = 'Insert a valid model. Available models from iphone 4 (2010) to iphone SE (2020). Input must be equal to: iphone 4\n iphone 4s\n iphone 5\n iphone 5s\n iphone 5c\n iphone 6\n iphone 6 plus\n iphone 6s\n iphone 6s plus\n iphone SE (1ª generación)\n iphone 7\n iphone 7 plus\n iphone 8\n iphone 8 plus\n iphone X\n iphone XS\n iphone XS Max\n iphone XR\n iphone 11\n iphone 11 pro\n iphone 11 pro Max\n iphone SE (2ª generación)" como por ejemplo'
            raise argparse.ArgumentTypeError(error)
    else:
        pass
'''
def validaDateFrom(dateFrom):#Validates that input date  is between 2010 and 2020 in variable dateFrom
    if dateFrom:    
        year = int(dateFrom[:4])
        print(year)
        correct_years = list(range(2009,2021,1))
        if year in correct_years:
            return dateFrom
        else:
            error = 'Introduce a date between 2010 and 2020 in YYYY-MM-DD format'
            raise argparse.ArgumentTypeError(error)
    else:
        pass

def validaDateTo(dateTo):#Validates that input date  is between 2010 and 2020 in variable dateTo
    if dateTo:
        year = int(dateTo[:4])
        print(year)
        correct_years = list(range(2009,2021,1))
        if year in correct_years:
            return dateTo
        else:
            error = 'Introduce a date between 2010 and 2020 in YYYY-MM-DD format'
            raise argparse.ArgumentTypeError(error)
    else:
        pass

def parse():
    parser = argparse.ArgumentParser(description="Introduce the date or the iPhone model and will analyze the impact of the introduction in Apple shares")
    
    parser.add_argument("-m", "--mail", dest='mail',#Parsing email (actualmente no tiene función)
                        default='mail unknown',
                        required=False,
                        help="Introduce your mail")

    parser.add_argument("-f","--dateFrom",#Parsing the "date from" for the analysis
                        dest="dateFrom",
                        type=validaDateFrom,
                        required=False,
                         help="Introduce the starting date for the analysis in format YYYY-MM-DD. Please, note that data is only available from 2010 so the input date must be equal or later ")
    parser.add_argument("-t","--dateTo",#Parsing the "date to" for the analysis
                        dest="dateTo",
                        type=validaDateTo,
                        required=False,
                        help="Introduce the ending date for the analysis in format YYYY-MM-DD. Please, note that data is only available until september 2020 so the input date must be equal or later ")
    parser.add_argument("-l","--model",#Parsing the iPhone model for the analysis
                        dest='model',
                        #type=validaModel,
                        required=False,
                        help="Introduce Iphone model. Available from iPhone 4 (2010) to iPhone SE (2020). Input must be equal to:\n iphone 4\n iPhone 4s\n iPhone 5\n iPhone 5s\n iPhone 5c\n iPhone 6\n iPhone 6 Plus\n iPhone 6s\n iPhone 6s Plus\n iPhone SE (1ª generación)\n iPhone 7\n iPhone 7 Plus\n iPhone 8\n iPhone 8 Plus\n iPhone X\n iPhone XS\n iPhone XS Max\n iPhone XR\n iPhone 11\n iPhone 11 Pro\n iPhone 11 Pro Max\n iPhone SE (2ª generación)")     
    args = parser.parse_args()                                                              
    return args

def main():
    args = parse()
    mail = args.mail#No se utiliza por falta de tiempo para desarrollar la función que mande el correo
    dateFrom = args.dateFrom
    dateTo = args.dateTo
    model = args.model
    print(args)

    if dateFrom and dateTo:#If date from and to are given, make an analysis by these dates
        df = gp.import_df()
        graph = gp.candle_dates(df,dateFrom,dateTo)
        stats = gp.df_stats(df)
        models = gp.models(dateFrom,dateTo)
        pdf.gen_PDF(dateFrom,dateTo)
        
        return graph, stats, models #If iPhone model is given, make the analysis taking this model as reference
    elif model:
        
        df = gp.import_df()
        date = gp.import_model(model)
        pres_date = gp.pres_date(date)
        pres_year = gp.pres_year(date)
        model_from = gp.model_from(pres_year)
        model_to = gp.model_to(pres_year)
        models = gp.models(model_from,model_to)
        graph1 = gp.candle_model(df,model_from,model_to, model,pres_date)
        graph2 = gp.line_model(df,model_from,model_to, model,pres_date)
        pdf.gen_PDF(dateFrom,dateTo)
        
    else:
        pass


if __name__ == "__main__":
    main()