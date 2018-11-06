import requests
from homeBlogData import extractBlogData
from singleTableDataExtraxtor import tableDataExtractor
from singleXpathDataExtractor import extractSinglePath

def getHomeBlogData(content, pathData, finalResult):
    print(pathData)
    if pathData.get('blogMainDivPath') and  pathData.get('blogPath') :
        finalResult["extraBlogData"] = extractBlogData(content, pathData.get('blogMainDivPath'), pathData.get('blogPath'))
    return finalResult
def getSingleTableDataExtractor(tableName, content, tablePath, finalResult):
    finalResult[tableName] = tableDataExtractor(content, tablePath)
    return finalResult

def getSingleXPathDataExtractor(content, singlePaths, finalResult):
    finalResult['singlePaths'] = extractSinglePath(content, singlePaths)

if __name__ == "__main__":

    # jsonFile = {
    #     "mainUrl":"https://www.dailysabah.com/search?key=politics",
    #     "homeBlogData": {
    #         'url': "https://www.dailysabah.com/search?key=politics",
    #         "blogMainDivPath": "body > section > form > div > div.table > div.right > div.searchList > ul",
    #         "blogPath": [['Heading', 'text',
    #                       'body > section > form > div > div.table > div.right > div.searchList > ul > li:nth-child(6) > a:nth-child(3) > span > strong']]
    #     }
    # }
    # jsonFile = {
    #     "mainUrl":"https://www.reuters.com/search/news?blob=bangalore+tech&sortBy=relevance&dateRange=pastYear",
    #     "homeBlogData": {
    #         'url': "https://www.reuters.com/search/news?blob=bangalore+tech&sortBy=relevance&dateRange=pastYear",
    #         "blogMainDivPath": "#content > section:nth-child(5) > div > div.column1.col.col-10 > div.module > div > div.search-result-list.news-search",
    #         "blogPath": [['Heading', 'text', '#content > section:nth-child(5) > div > div.column1.col.col-10 > div.module > div > div.search-result-list.news-search > div:nth-child(1) > div > h3'],
    #                      ['Data', 'text', '#content > section:nth-child(5) > div > div.column1.col.col-10 > div.module > div > div.search-result-list.news-search > div:nth-child(1) > div > div'],
    #                      ['Date', 'text', '#content > section:nth-child(5) > div > div.column1.col.col-10 > div.module > div > div.search-result-list.news-search > div:nth-child(1) > div > h5']]
    #     }
    #
    # }

    jsonFile = {
        "mainUrl": "https://www.w3schools.com/html/html_tables.asp",
        "homeBlogData": {
            'url': "https://www.reuters.com/search/news?blob=bangalore+tech&sortBy=relevance&dateRange=pastYear",
            "blogMainDivPath": "#main > ul",
            "blogPath": [['Heading', 'text','#main > ul > li:nth-child(1)'],
                         ['Data', 'text','#main > ul > li:nth-child(1) > code']
            ]

        },
        "tableData":[
            ['name1', '//*[@id="main"]/div[3]/div']
        ],
        "singlePath":[['Heading', 'text', '//*[@id="main"]/h2[1]'],
                      ['SubHeading', 'text', '//*[@id="main"]/h2[2]']]

    }

    finalResult = dict()
    content = requests.get(jsonFile.get('mainUrl')).content
    if jsonFile.get("homeBlogData"):
        getHomeBlogData(content, jsonFile.get("homeBlogData"), finalResult)

    if jsonFile.get('tableData'):
        for table in jsonFile.get('tableData'):
            getSingleTableDataExtractor(table[0], content, table[1], finalResult)

    if jsonFile.get('singlePath'):
        getSingleXPathDataExtractor(content, jsonFile.get('singlePath'), finalResult)
    print(finalResult)