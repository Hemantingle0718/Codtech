import os
from fpdf import FPDF

# Function to read data from file
def read_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            product_name = parts[0].strip()
            quantity_sold = int(parts[1].strip())
            price_per_unit = float(parts[2].strip())
            data.append((product_name, quantity_sold, price_per_unit))
    return data

# Function to analyze data (calculate total sales for each product)
def analyze_data(data):
    analysis = []
    for product_name, quantity_sold, price_per_unit in data:
        total_sales = quantity_sold * price_per_unit
        analysis.append((product_name, quantity_sold, price_per_unit, total_sales))
    return analysis

# Function to generate PDF report
def generate_pdf(analysis, output_pdf_path):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Add Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Sales Report", ln=True, align='C')

    # Add Sub-title
    pdf.set_font("Arial", 'I', 12)
    pdf.cell(200, 10, txt="Product-wise Sales Analysis", ln=True, align='C')
    pdf.ln(10)

    # Add Table Header
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(50, 10, 'Product Name', border=1, align='C')
    pdf.cell(50, 10, 'Quantity Sold', border=1, align='C')
    pdf.cell(50, 10, 'Price Per Unit', border=1, align='C')
    pdf.cell(50, 10, 'Total Sales', border=1, align='C')
    pdf.ln(10)

    # Add Data to the Table
    pdf.set_font("Arial", '', 12)
    for product_name, quantity_sold, price_per_unit, total_sales in analysis:
        pdf.cell(50, 10, product_name, border=1, align='C')
        pdf.cell(50, 10, str(quantity_sold), border=1, align='C')
        pdf.cell(50, 10, f"${price_per_unit:.2f}", border=1, align='C')
        pdf.cell(50, 10, f"${total_sales:.2f}", border=1, align='C')
        pdf.ln(10)

    # Output PDF
    pdf.output(output_pdf_path)

# Main function to tie everything together
def main():
    # Path to the input data file
    input_file = 'data.txt'
    
    # Path to the output PDF
    output_pdf = 'sales_report.pdf'
    
    # Read and analyze the data
    data = read_data(input_file)
    analysis = analyze_data(data)
    
    # Generate the PDF report
    generate_pdf(analysis, output_pdf)
    print(f"Report generated successfully: {output_pdf}")

if __name__ == "__main__":
    main()
