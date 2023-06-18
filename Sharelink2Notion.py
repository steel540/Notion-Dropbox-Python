import os
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()  # 載入環境變數

# 建立 Notion Client 物件
notion = Client(auth="Your_Notion_Token")

# 設定 Notion Database ID
database_id = "be1c915648344489a23480691e0f1427"
              

def update_processing_states(state_name, url):
    # 取得資料庫中的所有資料
    results = notion.databases.query(database_id).get("results")
    page_id = results[0]["id"]

    # 更新 processing states 欄位中的狀態為 state_name
    notion.pages.update(
        **{
            "page_id": page_id,
            "properties": {
                "Done": {
                    "select": {
                        "name": state_name
                    }
                },
                "Dropbox_share_link": {
                    "url": url
                }
            }
        }
    )

    # 印出更新後的訊息
    print(f"Processing states 欄位已更新為 {state_name}")
    print(f"Attached file by AI 欄位已上傳為 {url}")


def update_attached_link(url, row_id):
    

    # 更新 processing states 欄位中的狀態為 state_name
    notion.pages.update(
        **{
            "page_id": row_id,
            "properties": {
                "Attached file by AI": {
                    "url": url
                }
            }
        }
    )

    # 印出更新後的訊息
    print(f"Attached_link 欄位已更新為 {url}") 

if __name__ == "__main__":
    # 設定 processing states 欄位內的狀態
    state_name = "fail"
    url = "https://www.dropbox.com/s/as67cfhhobzpm1p/slas382a.pdf?dl=0"

    # 呼叫副程式更新 Notion 資料庫中的 processing states 欄位
    update_processing_states(state_name, url)
    #update_attached_link(url, '84d2ebf2-4e53-45a6-9121-dbea0ec6741f')

