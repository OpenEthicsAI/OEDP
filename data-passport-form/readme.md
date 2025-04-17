
# JSON Schema Form Generator

A lightweight tool that generates web forms from JSON Schema definitions. This tool allows users to create, validate, and collect form submissions based on JSON Schema specifications.

## 🚀 Features

- Dynamically generates forms from JSON Schema
- Supports schema validation according to JSON Schema specification
- Handles nested objects and arrays
- Resolves JSON Schema references recursively
- Form submissions can be downloaded as JSON or CSV
- Converts GitHub URLs to raw GitHub URLs automatically
- Validation respects schema requirements (formats, patterns, etc.)

## 🧩 Usage

1. Enter a JSON Schema URL or paste a schema directly
2. Click **"Fetch Schema"** or **"Generate Form"**
3. Fill out the generated form
4. Submit the form to collect data
5. Download submissions as JSON or CSV

## 🌐 Example URLs

- Raw GitHub URL:  
  `https://raw.githubusercontent.com/OpenEthicsAI/OEDP/refs/heads/main/schema/oedp.passport.schema.json`

## ⚠️ CORS Handling

When working with external schema URLs, you may encounter **CORS (Cross-Origin Resource Sharing)** restrictions. To work around this:

- Use **raw GitHub URLs** whenever possible (they bypass CORS issues)
- Copy and paste the schema directly into the text area

## 🛠️ Local Development

To run this tool locally:

1. Clone the repository
2. Open the HTML file in a web browser

