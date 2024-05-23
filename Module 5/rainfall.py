


if __name__ == "__main__":
    years = int(input("Enter the number of years: "))
    total_rainfall = 0
    for i in range(years):
        for z in range(12):
            inches = int(input("How many inches of rainfall in month {}:".format(z+1)))
            total_rainfall += inches
    
    month_count = years * 12
    avg_rainfall = total_rainfall/month_count
    
    print("# of Months:", month_count)
    print("Total Inches of Rainfall:", total_rainfall)
    print("Average Rainfall per Month:", avg_rainfall)