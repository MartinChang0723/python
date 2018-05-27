def readPDF(pdfFile):
  from PyPDF2 import PdfFileReader
  return PdfFileReader(pdfFile)

def main():
  from urllib import request
  from urllib.request import urlopen
  from bs4 import BeautifulSoup
  import ssl
  import io
  context = ssl._create_unverified_context() 
  query = input("Keyword? ")
  req = request.Request(
    "https://www.google.com.tw/search?q=" + query + "+filetype%3Apdf", 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
  )
  urlContent = urlopen(req, context=context).read()
  s = BeautifulSoup(urlContent, "lxml")
  target = s.select("#rso > div > div > div > div > div > h3 > a")
  # for tar in target:
  #   link = tar.attrs["href"]
  #   pdfFile = urlopen(link)
  #   outputString = readPDF(pdfFile)
  #   print(outputString)
  #   pdfFile.close()
  link = target[0].attrs["href"]
  pdfFile = io.BytesIO(urlopen(link, context=context).read())
  outputString = readPDF(pdfFile)
  print(outputString)
  pdfFile.close()


  # from urllib.request import urlopen
  # #url = "http://pythonscraping.com/pages/warandpeace/chapter1.pdf"
  # #url = "https://tools.ietf.org/pdf/rfc8369.pdf"
  # url = "http://secret.nchu.edu.tw/download/65-1020514.pdf"
  # pdfFile = urlopen(url)
  # # To retrieve a local PDF file, you may replace the above statement as
  # # pdfFile = open("test1.pdf", "rb")
  # outputString = readPDF(pdfFile)
  # print(outputString)
  # pdfFile.close()

if __name__ == "__main__":
  main()