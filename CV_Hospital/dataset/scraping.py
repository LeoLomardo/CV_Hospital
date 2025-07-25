from icrawler.builtin import GoogleImageCrawler

keywords = [
    'icu bed top view'
]

for keyword in keywords:
    folder_name = keyword.replace(" ", "_").lower()
    google_crawler = GoogleImageCrawler(
        storage={'root_dir': f'/home/leo/Documentos/LES/CV_Hospital/CV_Hospital/dataset/Por fazer/{folder_name}'}
    )
    
    print(f"Baixando imagens para: {keyword}")
    google_crawler.crawl(
        keyword=keyword,
        max_num=500,  
        file_idx_offset=0
    )
