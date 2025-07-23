from icrawler.builtin import GoogleImageCrawler

keywords = [
    'hospital bed top view',
    'icu bed',
    'empty hospital bed',
    'hospital bed side view',
    'hospital bed'
]

for keyword in keywords:
    folder_name = keyword.replace(" ", "_").lower()
    google_crawler = GoogleImageCrawler(
        storage={'root_dir': f'/home/leo/Documentos/LES/CV_Hospital/CV_Hospital/dataset/images/{folder_name}'}
    )
    
    print(f"Baixando imagens para: {keyword}")
    google_crawler.crawl(
        keyword=keyword,
        max_num=200,  
        file_idx_offset=0
    )
