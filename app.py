import joblib
import pickle
from flask import Flask, render_template, request
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)


# Load the first pickle file
import joblib

# Load the model using joblib
random_forest_model = joblib.load('random_forest_model.pkl')
decision_tree_model = joblib.load('decision_tree_model.pkl')

@app.route('/')
def index():
    return render_template('about.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the HTML form
        # Get form data
    sttl = float(request.form['sttl'])
    swin = float(request.form['swin'])
    dwin = float(request.form['dwin'])
    dpkts = float(request.form['dpkts'])
    spkts = float(request.form['spkts'])
    dload = float(request.form['dload'])
    ct_dst_src_ltm = float(request.form['ct_dst_src_ltm'])
    dloss = float(request.form['dloss'])
    ct_src_dport_ltm = float(request.form['ct_src_dport_ltm'])
    ct_dst_sport_ltm = float(request.form['ct_dst_sport_ltm'])
    stcpb = float(request.form['stcpb'])
    dtcpb = float(request.form['dtcpb'])
    ct_srv_dst = float(request.form['ct_srv_dst'])
    ct_srv_src = float(request.form['ct_srv_src'])
    dbytes = float(request.form['dbytes'])
    ct_dst_ltm = float(request.form['ct_dst_ltm'])
    ct_src_ltm = float(request.form['ct_src_ltm'])
    sloss = float(request.form['sloss'])
    dmean = float(request.form['dmean'])
    dttl = float(request.form['dttl'])
    

    # Perform prediction using the loaded models
    prediction_rf = None
    prediction_dt = None
    input_features=[[sttl, swin, dwin, dpkts, spkts, dload, dloss, dttl,
                                                          ct_dst_src_ltm, stcpb, dtcpb, dbytes, ct_dst_sport_ltm,
                                                          ct_src_dport_ltm, dmean, ct_srv_dst, sloss, ct_srv_src,
                                                          ct_src_ltm, ct_dst_ltm]]
    # Create a StandardScaler instance
    scaler = StandardScaler()

# Fit and transform the scaler on the training data
    input_features_scaled = scaler.fit_transform(input_features)
    

    if random_forest_model:
        try:
            prediction_rf = random_forest_model.predict(input_features_scaled )
        except:
            print("Error during Random Forest prediction.")

    if decision_tree_model:
        try:
            prediction_dt = decision_tree_model.predict(input_features_scaled )
        except:
            print("Error during Decision Tree prediction.")

    # Pass the prediction results to the HTML page
    return render_template('result.html', prediction_rf=prediction_rf, prediction_dt=prediction_dt)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
