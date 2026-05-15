    import uuid

    DB=[]

    def Add_To_List(data):
        data['id']=str(uuid.uuid4())
        DB.append(data)
        return data


    def All_Movies():
        return DB

    def search(id):
        for i in DB:
            if i['id']==id:
                return i
        return None

    def delete(id):
        for i in DB:
            if i['id'] ==id:
                DB.remove(i)
                return True
        return False

    def update(id,data):
        for i in DB:
            if i['id']==id:
                DB['id']=data
                return DB[id]
        return None