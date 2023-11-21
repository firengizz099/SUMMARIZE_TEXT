# SUMMARIZE_TEXT_LLM
![App Screenshot](https://github.com/firengizz099/SUMMARIZE_TEXT/blob/main/ylxiong_0-1628032473948.png?raw=true)

**Bu kod, belirli bir PDF dosyasını indirip açarak metni özetlemek için Python dilinde yazılmıştır.**
**İlk olarak, gerekli Python kütüphanelerini içe aktarırız:**
**1) requests: Web üzerinden PDF dosyasını indirmek için kullanılır.**
**2) openai: OpenAI API ile etkileşimde bulunmak için kullanılır.**
**3) fitz: PyMuPDF kütüphanesi ile PDF dosyasını işlemek için kullanılır.**
**4) API anahtarınızı ve hedef PDF dosyasının URL'sini belirtmelisiniz:**
**5) api_key: OpenAI API'ye erişim sağlamak için kullanılacak API anahtarınızı içerir. Bu anahtarı OpenAI'den almalısınız.**
**6) pdf_url: Özetlemek istediğiniz PDF dosyasının URL'sini içerir.**
**download_and_open_pdf fonksiyonu, belirtilen PDF URL'sini indirir ve açar. Bu işlev aşağıdaki görevleri gerçekleştirir:**
**7) requests.get(pdf_url): PDF dosyasını belirtilen URL'den indirir.**
**8) open("downloaded_pdf.pdf", "wb"): İndirilen PDF dosyasını yerel bir dosyaya kaydeder.**
**9) fitz.open("downloaded_pdf.pdf"): PyMuPDF kullanarak PDF dosyasını açar.**
**PDF dosyasının her sayfasındaki metni birleştirerek bir dize (pdf_text) oluşturur.**
**pdf_text dizesini döndürür.**
**summarize_text fonksiyonu, belirtilen metni özetlemek için OpenAI API'sini kullanır. Bu işlev aşağıdaki görevleri gerçekleştirir:**
**openai.api_key = api_key: API anahtarını belirtilen anahtarla ayarlar.**
**openai.Completion.create(...): OpenAI API'sini kullanarak metni özetler. Özetleme işlemi GPT-3.5 (Davinci) motorunu kullanır ve belirli parametreleri ayarlar.**
**Özetlenmiş metni alır ve bu metni döndürür.**
**Ana program başlar ve aşağıdaki işleri yapar:**
**download_and_open_pdf(pdf_url): PDF dosyasını indirir ve açar, ardından pdf_text adlı bir metin dizesine kaydeder.**
10) (summarize_text(pdf_text): pdf_text metnini özetler ve sonucu pdf_summary adlı bir metin dizesine kaydeder.
11) print("PDF Özeti:"): Özetlenmiş metni ekrana yazdırır.
with open("new_pdf.txt", "w"): Özetlenmiş metni "new_pdf.txt" adlı bir dosyaya kaydeder.
