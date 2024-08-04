txt = input("Text: ")
sub = input("Substring: ")

def checkacr(txt,sub):
    global flag
    flag = False
    for i in range(len(txt)):
        cur_mis = 0
        if txt[i] == sub[0]:
            for j in range(len(sub)):
                try:
                    if txt[i+j] == sub[j]:
                        pass
                    else:
                        cur_mis += 1
                except:
                    cur_mis += 1
            if cur_mis == 0:
                flag = True
                break
            elif cur_mis != 0:
                pass
def checksub(txt,sub):
    result = []
    if flag == True:
        for i in range(len(txt)):
            cur_mis = 0
            try:
                if txt[i] == sub[0]:
                    for j in range(len(sub)):
                        try:
                            if txt[i+j] == sub[j]:
                                pass
                            else:
                                cur_mis += 1
                        except:
                            cur_mis += 1
                    if cur_mis == 0:
                        result.append(f'[{txt[i:i+len(sub)]}]')
                        txt = txt[:i]+txt[i+len(sub):]
                        
                    elif cur_mis != 0:
                        result.append(txt[i])
                        pass
            except:
                pass
            try:
                if txt[i] != sub[0]:
                    result.append(txt[i])
            except IndexError:
                pass
    if flag == False:
        for i in range(len(txt)):
            cur_mis = 0
            try:
                if txt[i] == sub[0]:
                    for j in range(len(sub)):
                        try:
                            if txt[i+j] == sub[j]:
                                pass
                            else:
                                cur_mis += 1
                        except:
                            cur_mis += 1
                    if cur_mis <= 1:
                        newtext = ''
                        for x in range(len(sub)):
                            if txt[i+x] == sub[x]:
                                newtext += txt[i+x]
                            else:
                                newtext += '?'
                        result.append(f'[{newtext}]')
                        txt = txt[:i]+' '+txt[i+len(sub):]
                        
                    elif cur_mis > 1:
                        result.append(txt[i])
                        pass
            except:
                pass
            try:
                if txt[i] != sub[0]:
                    if txt[i] != ' ':
                        result.append(txt[i])
            except IndexError:
                pass
    return result
    
checkacr(txt,sub)
for i in checksub(txt,sub):
    print(i,end='')