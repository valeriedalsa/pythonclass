def main():
    original = (float(input("How much was your purchase? ")))
    county_sales_tax = original * 0.025
    state_sales_tax = original * 0.05
    total = state_sales_tax + county_sales_tax + original
    print(f'''Your purchase was = ${original:,.2f} 
Your state sales tax for this purchase is = ${state_sales_tax:,.2f}
Your county tax is = ${county_sales_tax:.2f}
Your total is = ${total:,.2f}''')
main()

                    
