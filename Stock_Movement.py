import pandas as pd
import re
from textblob import TextBlob

file_path = "telegram_Messages_official_samco_20241207_105834.csv"
df = pd.read_csv(file_path, names=["Date", "Sender", "Message"])


def extract_stock_details(Message):
    stock_details = {
        "Stock Name": None,
        "Symbol": None,
        "Recommendation": None,
        "CMP": None,
        "Stop Loss": None,
        "Target": None,
        "Duration": None,
        "Sentiment": None
    }

    name_match = re.search(r"Stock Name: ([^\n]*)", Message)
    if name_match:
        stock_details["Stock Name"] = name_match.group(1).strip()

 
    symbol_match = re.search(r"Symbol: ([^\n]*)", Message)
    if symbol_match:
        stock_details["Symbol"] = symbol_match.group(1).strip()


    recommendation_match = re.search(r"Rating: (Buy|Sell|Hold)", Message)
    if recommendation_match:
        stock_details["Recommendation"] = recommendation_match.group(1).strip()

    cmp_match = re.search(r"CMP: \u20b9?([0-9]+)", Message)
    if cmp_match:
        stock_details["CMP"] = int(cmp_match.group(1))


    stop_loss_match = re.search(r"Stop loss: \u20b9?([0-9]+)", Message)
    if stop_loss_match:
        stock_details["Stop Loss"] = int(stop_loss_match.group(1))


    target_match = re.search(r"Target: ([0-9]+)", Message)
    if target_match:
        stock_details["Target"] = int(target_match.group(1))

  
    duration_match = re.search(r"Duration: ([^\n]*)", Message)
    if duration_match:
        stock_details["Duration"] = duration_match.group(1).strip()

  
    stock_details["Sentiment"] = TextBlob(Message).sentiment.polarity

    return stock_details


def determine_stock_movement(sentiment):
    if sentiment >= 0:
        return "Upward"
    elif sentiment < 0:
        return "Downward"
    


print(df["Message"])
stock_data = df.apply(lambda row: {**extract_stock_details(str(row["Message"])), "Date": row["Date"]}, axis=1)


stock_df = pd.DataFrame(stock_data.tolist())
stock_df = stock_df.dropna(subset=["Stock Name"])


print(stock_df)

stock_df["Stock Movement"] = stock_df["Sentiment"].apply(determine_stock_movement)

output_file = "stock_analysis_with_date.csv"
stock_df.to_csv(output_file, index=False)
print(f"Analysis saved to {output_file}")


