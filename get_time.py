

def get_time(date,start_time,end_time):         #format = '2024-06-16T21:00:00'
    
    day=date[0]+date[1]
    month=date[2]+date[3]
    start=''
    end=''

    start='2024-'+month+'-'+day+'T'+start_time+':00'
    end='2024-'+month+'-'+day+'T'+end_time+':00'
    return(start, end)

print(get_time('1606','12:00','16:00'))
