# Invoice QR Code Generator

## Overview

The "**Invoice QR Code Generator**" is a Python application designed to simplify invoice management by allowing users to generate QR codes for their invoices. This project provides an efficient and user-friendly solution for small-scale invoicing tasks.

## Features

- **User-Friendly Interface**: The application prompts users to input essential invoice details, ensuring an intuitive and hassle-free experience.

- **QR Code Generation**: It utilizes the `pyqrcode` library to convert invoice details into QR codes. QR codes provide a convenient way to store and retrieve information.

- **Customization**: Users can enter a unique QR code name, making it easy to identify and manage multiple invoices.

- **Total Amount Calculation**: The project calculates the total amount by summing up individual item amounts, streamlining the invoicing process.

## Usage

1. **Client Details**: Enter the client's name, invoice date, due date, invoice number, and PO number.

2. **Item Descriptions**: Provide item descriptions, quantities, and amounts for your invoice. The application supports up to five items.

3. **Total Amount**: Enter the overall amount for all quantities.

4. **QR Code Name**: Choose a name for your QR code to facilitate easy identification.

5. **Payment Mode**: Specify the payment mode, such as "Paytm" or "Paypal."

6. **Generate QR Code**: The application processes your inputs and generates a QR code containing all invoice details.

## Benefits

- **Efficiency**: Invoice details can be quickly accessed by scanning the generated QR code, reducing the need for manual data entry.

- **Organization**: The custom QR code names make it easy to manage multiple invoices effectively.

- **Data Integrity**: Validation checks ensure that user inputs are accurate and complete.

## Future Enhancements

- Inclusion of additional invoice details.
- Improved error handling and reporting.
- Support for a broader range of payment modes.


## Author

[Kandukuri Charan](https://github.com/Charan513)
