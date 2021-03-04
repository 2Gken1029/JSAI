#!python3

def counterMethod(morphologicalAnalysis_list, variable_list, excel_sheet):
    count_list =[]
    if excel_sheet == '../wordTime_train.xlsx':
        time_word = ["今","今回","すぐ","今日"]
        for list in morphologicalAnalysis_list: # 1ファイルの形態素リストを1行ごとにみていく
            if set(time_word) & set(list): # 形態素リストの中に時間リストと重複する単語をみる
                duplicates = set(time_word) & set(list)
                for duplicate in duplicates: # 重複数に応じる
                    if duplicate == "今":
                        ima = variable_list[0]
                        for word in list:
                            if word in ima:
                                count_list.append(ima[word])
                    elif duplicate == "今回":
                        konkai = variable_list[1]
                        for word in list:
                            if word in konkai:
                                count_list.append(konkai[word])
                    elif duplicate == "すぐ":
                        sugu = variable_list[2]
                        for word in list:
                            if word in sugu:
                                count_list.append(sugu[word])
                    elif duplicate == "今日":
                        kyou = variable_list[3]
                        for word in list:
                            if word in kyou:
                                count_list.append(kyou[word])                        
    elif excel_sheet == '../wordHigh_train.xlsx':
        highscore_word = ["電話","確認","連絡","お願い"]
        for list in morphologicalAnalysis_list: # 1ファイルの形態素リストを1行ごとにみていく
            if set(highscore_word) & set(list): # 形態素リストの中に頻出リストと重複する単語をみる
                duplicates = set(highscore_word) & set(list)
                for duplicate in duplicates: # 重複数に応じる
                    if duplicate == "電話":
                        ima = variable_list[0]
                        for word in list:
                            if word in ima:
                                count_list.append(ima[word])
                    elif duplicate == "確認":
                        konkai = variable_list[1]
                        for word in list:
                            if word in konkai:
                                count_list.append(konkai[word])
                    elif duplicate == "連絡":
                        sugu = variable_list[2]
                        for word in list:
                            if word in sugu:
                                count_list.append(sugu[word])
                    elif duplicate == "お願い":
                        kyou = variable_list[3]
                        for word in list:
                            if word in kyou:
                                count_list.append(kyou[word])
    return count_list