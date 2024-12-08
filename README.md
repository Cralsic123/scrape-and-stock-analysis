# **Stock Movements Analysis and Prediction**

## **Project Overview**
This project leverages data scraped from Telegram groups to analyze stock movements and predict their future trends based on sentiment analysis. Using tools like `Telethon` for data collection and `TextBlob` for sentiment analysis, the project processes financial recommendations, extracts meaningful information, and predicts stock movements.

The workflow consists of:
1. **Data Collection**: Telegram messages containing stock recommendations are scraped and stored in CSV format.
2. **Stock Movement Extraction**: Extracts stock-specific details such as stock name, symbol, CMP, target prices, and sentiment polarity from messages.
3. **Exploratory Data Analysis (EDA)**: Conducts analysis on stock trends, sentiment scores, and performance.
4. **Prediction Modeling**: Builds a machine learning model to predict stock movements (upward or downward) based on historical and sentiment data.

---

## **Key Components**

### **1. Stock Movement Extraction**
**File**: `Stock_Movement.py`  
This script processes the raw messages dataset and performs:
- **Text Parsing**:
  - Extracts key stock details such as Name, Symbol, CMP, Stop Loss, Target, Recommendation, and Duration using regex.
  - Uses `TextBlob` to calculate sentiment polarity for each message.
- **Movement Determination**:
  - Maps positive sentiment to "Upward" and negative sentiment to "Downward" movement predictions.
- **Output**:
  - Saves the processed data into a CSV file named `stock_analysis_with_date.csv`.

---

### **2. Data Analysis**
**File**: `analysis.ipynb`  
This notebook performs exploratory analysis and visualizations to uncover insights:
- **Price Trends**: Tracks stock movement trends over time.
- **Sentiment vs. Movement Correlation**: Analyzes the relationship between sentiment scores and predicted movements.
- **Descriptive Statistics**: Summarizes key metrics such as average CMP, target prices, and sentiment scores.
- **Recommendation Performance**: Examines how stock performance aligns with short-term or long-term recommendations.

---

### **3. Prediction Model**
**File**: `Prediction_Model.ipynb`  
This notebook builds a predictive model to forecast stock movements:
- **Features**:
  - Includes CMP, sentiment scores, targets, stop loss, and recommendation duration.
- **Modeling Process**:
  - Splits data into training and testing sets.
  - Implements machine learning algorithms like Logistic Regression, Random Forests, or Neural Networks.
- **Output**:
  - Predicts stock movements (upward or downward) and provides probability scores for predictions.

---

## **Installation and Dependencies**

To run this project, ensure you have the following dependencies installed in your Python environment. You can install them using the provided `requirements.txt` file.

### **Required Libraries**
1. **Python Environment**
   - Python 3.8 or later.
2. **Data Handling and Processing**:
   - `pandas`: Data manipulation and analysis.
   - `numpy`: Numerical computations.
3. **Text Analysis**:
   - `TextBlob`: Sentiment analysis and polarity calculation.
4. **Visualization**:
   - `matplotlib`: Plotting and visualizing data.
   - `seaborn`: Enhanced data visualization.
5. **Machine Learning (for Prediction)**:
   - `scikit-learn`: Model building and evaluation.
6. **Telegram API**:
   - `Telethon`: Scraping messages from Telegram groups.
7. **Environment Management**:
   - `python-dotenv`: To securely manage API keys in a `.env` file.
8. **Other Utilities**:
   - `re`: Regular expressions for text parsing.

---

### **Setting Up**
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>

2. Set up your Telegram API credentials: Add your API ID and API Hash to a `.env` file in the root directory and then run the scraping.py file.

3. Then, run the data analysis `ipynb` to look into the analysis of the stocks through the texts of the Telegram channels.
  
4. In the end run the prediction file to load the model. At first I have used just random classifier but then I have included an ensemble and a grid search algorithm for better fine tuning and finding hyperparameters
