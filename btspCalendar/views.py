from django.shortcuts import render,redirect
import calendar
from calendar import HTMLCalendar
import datetime
from datetime import date
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import JsonResponse
import json
# Create your views here.


#forms



def prevOrNextMonth(request):


        

        if request.method=="POST" :

         
            #gettting DAta
            getData = json.loads(request.body)

            #assgin year and month
            current_year=getData['current_year']
            current_month=getData['current_month']
            value=getData['value']

            year=int(current_year)
            #month capitalize
            month = current_month.capitalize()
            #month no fetch
            month_no=list(calendar.month_name).index(month)

            if value=="nextbutton":
                month_no=month_no+1
                if(month_no>12):
                        year=year+1
                        month_no=1
            elif value=="prevbutton":
                month_no=month_no-1
                if(month_no<1):
                        year=year-1
                        month_no=12
            elif value=="gotoButton":
                 month_no=month_no
                  

                        
            #generate month
            month=calendar.month_name[(month_no)]
            #generate calender
            calend=HTMLCalendar().formatmonth(
                        year,
             (month_no))
            #return response
            return JsonResponse({ 
                               'message':'sucess',
                               'month':month,
                               'year':year,
                               'calend':calend,
                                        })
           

        




#current date - HOme function
def btspcalendar(request):
            current_year = date.today().year
            current_month=date.today().month
            #generate month
            current_month=calendar.month_name[(current_month)]

            current_month = current_month.capitalize()
            month_no=list(calendar.month_name).index(current_month)
            calend=HTMLCalendar().formatmonth(
            current_year,
            month_no)

            months=list(calendar.month_name) 

           
    
            return render(request,'btspcalendar.html', { 
                    "months":months,
                    "current_year":current_year,
                    'range': range(2051),
                    "current_month":current_month,
                    "current_year":current_year,
                    "month":current_month,
                    "calend":calend,
                    })

