import requests
import openai
import fitz  # PyMuPDF

# OpenAI API anahtarınızı buraya ekleyin
api_key = "YOUR_API"

# PDF dosyasının URL'sini buraya ekleyin
pdf_url = "https://web.itu.edu.tr/~sonmez/lisans/ai/yapay_zeka_icerik1_1.6.pdf"

# PDF dosyasını indirin ve açın
def download_and_open_pdf(pdf_url):
    response = requests.get(pdf_url)
    with open("downloaded_pdf.pdf", "wb") as pdf_file:
        pdf_file.write(response.content)
    
    pdf_text = ""
    doc = fitz.open("downloaded_pdf.pdf")
    for page_num in range(doc.page_count):
        page = doc[page_num]
        pdf_text += page.get_text()
    
    return pdf_text

# Metni özetlemek için OpenAI API'sini kullanın
def summarize_text(text):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="davinci",  # GPT-3.5'i kullanabilirsiniz
        prompt=text[:2048],  # Girişi modelin maksimum bağlam uzunluğuna sığacak şekilde kısalttık
        max_tokens=1000,  # İstenen özetin maksimum uzunluğunu belirleyin
        temperature=0.7,  # Daha fazla veya daha az yaratıcılık isteğinize göre değiştirin
    )
    summary = response.choices[0].text.strip()
    return summary

# PDF dosyasını indirin ve açın
pdf_text = download_and_open_pdf(pdf_url)

# PDF metnini özetleyin
pdf_summary = summarize_text(pdf_text)

# Sonucu terminalde gösterin
print("PDF Özeti:")
print(pdf_summary)

# Aynı çıktıyı "new_pdf.txt" adlı bir dosyaya kaydedin
with open("new_pdf.txt", "w") as output_file:
    output_file.write(pdf_summary)




