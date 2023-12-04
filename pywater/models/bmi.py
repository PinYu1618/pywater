def BMI(height, weight) -> str:
    # 計算BMI
    bmi = round(float(weight) / float(height) ** 2, 2)
    # 判斷BMI
    if bmi < 18.5:
        warning = "過輕，建議增加飲食營養和適量運動。"
    elif 18.5 <= bmi < 24:
        warning = "正常，保持良好的生活習慣，繼續保持健康。"
    elif 24 <= bmi < 27:
        warning = "過重，建議注意飲食並增加運動，以維持健康體重。"
    elif 27 <= bmi < 30:
        warning = "輕度肥胖，建議諮詢醫生，並進行適當的飲食和運動調整。"
    elif 30 <= bmi < 35:
        warning = "中度肥胖，建議尋求專業的醫療建議，制定科學的減重計畫。"
    else:
        warning = "重度肥胖，請立即諮詢專業醫生，並進行相應的治療。"

    return str(bmi) + " " + warning
