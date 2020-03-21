import datetime
import time

while True:
    choice = input('Begin E to exit, any other key to begin another Pomodoro. ')
    if choice == 'E':
        print('\nExiting application...\n')
        break
    else:
        start = time.time()
        last = start
        completedPomNum = 0
        incompletePomNum = 0
        totaltimeworked = 0
        try:
            print('\nPress ENTER to begin Pomodoro')
            input()
            print('Beginning Pomodoro...')
            while True:
                delta = datetime.timedelta(days=0, hours=0, minutes=30, seconds=0)
                if time.time() - start >= delta.total_seconds():
                    print('Pomodoro successfully completed')
                    completedPomNum += 1
                    totaltimeworked += round((time.time() - start), 2)
                    with open('worklog.txt','a') as wl:
                        wl.write(f'DATE:  {str(datetime.date.today())} WORKED:  {round(totaltimeworked % 60,2)} MIN\n')
                    break
        except KeyboardInterrupt:
            incompletePomNum += 1
            print(f'You worked for {round((time.time()-start)/60, 2)} minutes')
            totaltimeworked += round((time.time()-start), 2)
            with open('worklog.txt', 'a') as wl:
                wl.write(f'DATE:  {str(datetime.date.today())} WORKED:  {round(totaltimeworked / 60,2)} MIN\n')
            print(f'Incomplete Pomodoro of length {round(totaltimeworked/60,2)} \n')


