from tkinter import *
import time
import tkinter.font as font
from PIL import Image, ImageTk
import random


#----- function to countdown timer -----#
def countdown(t):
    print('Countdown until next exercise...')
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\n\r")
        time.sleep(1)
        t -= 1
        if (t == 0):
            print('\nIt is time for some stretches!!')
            #show the exercise panel
            displayExercisePanel()           
#----- end of function countdown() -----#
  
#----- function to iterate through the dictionary -----#
def iterateDict(dct, win, ct):  
    for key, val in dct.items():
        #check if value is another dictionary, and if iterate again
        if isinstance(val, dict):
            iterateDict(val,win,ct)
        else:
            if key.find("msg")!=-1:
                print("*** start of message ***", val, "*** end of message ***")
                text_label = Label(win,
                    text = val,
                    fg = '#ccd5de',
                    bg = '#243f5c', #99cdde',
                    width = '108',
                    height = '15',                    
                    justify = LEFT,
                    font = ('Helvetica', 11, 'bold'))
                text_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)
                
            else:
                print("Image Path is", val);
                imgList[ct] = val
                ct += 1
#----- end of iterateDict() function -----#

         

#----- Main section -----#

#define global arrays for image path
global imgList
imgList = ["a","b"]

window = Tk()
window.geometry("1000x950+25+25")
window.configure(bg='#99cdde')
window.title("Ergonomical Work Instructions")

btnFont = font.Font(family='Helvetica', size=14, weight='bold')
imageLabel = Label(window, image='')

#initializing exercise dictionary
exerciseDetails = {
    "exercise1": {
                  "msg":('\n\nExercise-1: NECK ROTATION\n\n'\
        '1. Stand tall with feet shoulder width apart\n'\
        '2. Gently rotate head to the side until you feel resistance in the neck\n'\
        '3. Hold position for a count of two\n'\
        '4. Turn head to other side as above\n'\
        'Repeat five times on each side\n\n'\
        'Benefits: It helps to loosen up, and reduce the heaviness and stiffness around the shoulders,\n'\
         'back of neck, eyes, and head\n'),
                    "img": {
                      "img1": "./Images/Neck1.jpg"
                       }
                  },
    "exercise2": {
                 "msg": ('\n\nExercise-2: SHOULDER ROTATIONS\n\n'\
        '1. Stand tall with feet shoulder width apart\n'\
        '2. Put palms together and interlink fingers\n'\
        '3. Keep arms straight, lift hands above head until resistance is felt in the shoulders\n'\
        '4. Hold for a count of two, then lower hands to starting position\n'\
        'Repeat 10 times\n\n'\
        'Benefits: It helps to relieve tightness, reduce tension, improve flexibility,\n'\
        'prevent injury in your shoulders\n'),
                    "img": {
                     "img1": "./Images/Shoulder1.jpg"                     
                    }
                 },
    "exercise3": {
                "msg": ('\n\nExercise-3: SIDE BENDS\n\n'\
        '1. Stand tall with feet shoulder width apart\n'\
        '2. Place one hand on the hip, the other above the head with arm straight\n'\
        '3. Stretch to the side with the hand above only until the first point of resistance in the back\n'\
        '4. Hold for 10 seconds\n'\
        'Do the same with your other side\n\n'\
        'Benefits: Strengthens the side ab wall. It helps to tightens the core and improves your posture and stability\n'),
                "img": {
                    "img1": "./Images/SideBend1.jpg"
                    }
                },
    "exercise4": {
                "msg": ('\n\nExercise-4: STRAIGHTEN YOUR ARM\n\n'\
            '1. Holding your fingers, gently bend wrist up until you feel a stretch in the forearm\n'\
            '2. Hold for 15 seconds then release\n\n'\
            'Repeat with your other arm\n\n'\
            'Benefits: It helps sore muscles to recover faster, improved shoulder joints flexibility, mobility, and range of motion \n'),
                "img": {
                    "img1": "./Images/Arm1.jpg"
                    }
                },
    "exercise5": {
                "msg": ('\n\nExercise-5: BACKWARDS ARCHING\n\n'\
            '1. Stand tall\n'\
            '2. Place both hands on lower back\n'\
            '3. Gently arch back until first point of resistance and hold for 15 seconds\n'\
                  'making sure you do not throw your head back\n' \
            'Repeat three times\n\n'\
            'Benefits: Reduces range of motion, increasing stability, and recruits other muscle groups to help generate more power\n'),
                "img": {
                    "img1": "./Images/Backwards1.jpg"                
                    }
            },
    "exercise6": {
                "msg": ('\n\nExercise-6: HEEL RISES\n\n'\
            '1. Stand tall and hold onto something for support, such as a chair\n'\
            '2. Lift both heels off the ground, coming up onto the balls of the feet\n'\
            '3. Hold raise for a count of two, then slowly lower heels to the ground\n\n'\
            'Repeat 15 times\n\n'\
            'Benefits: Heel raises strengthen the calf muscles\n\n'),
                "img": {
                    "img1": "./Images/Heel1.jpg"
                    }
        },
    "exercise7": {
                "msg": ('\n\nExercise-7: TRICEP DIPS\n\n'\
                '1. Stand with a chair (that doesn\'t have wheels!) behind you\n'\
                '2. Put your plams flat on the chair, with your fingers facing away from you.\n'\
                'Keep your heels on the ground with your legs straight out in fron of you\n'\
                '3. Lower yourself until your upper arms are almost parallel to the ground\n\n'\
                'Return to the starting position and repeat for atleast 10 reps\n\n'\
                '\nMuscle groups worked: Triceps and Chest\n'),
                "img": {
                    "img1": "./Images/Tricepdips1.jpg"
                    }
            },
    "exercise8": {
                "msg": ('\n\nExercise-8: DESK PUSH UPS\n\n'\
                '1. Face your desk and lean against it, with your hands\n'\
                    'slightly wider than your shoulders and your arms straight\n'\
                '2. Lower yourself until your chest almost reaches your desk, then return to the starting position\n'\
                'Repeat for atleast 10 repetitions\n\n'\
                '\nMuscle groups worked: Triceps and Chest\n'),
                "img": {
                    "img1": "./Images/Pushups1.jpg"
                    }
            },
    "exercise9": {
                "msg": ('\n\nExercise-9: CALF RAISES\n\n'\
                '1. Stand tall and hold your chair or desk for balance\n'\
                '2. Rise up onto your toes, hold for a moment, and then lower your heels back to the floor\n'\
                'Repeat for atleast 10 repetitions\n\n'\
                '\nMuscle groups worked: Calves\n'),
                "img": {
                    "img1": "./Images/Calf1.jpg"
                    }
            },
     "exercise10": {
                "msg": ('\n\nExercise-10: CHAIR OR DESK PLANKS\n\n'\
                '1. With your body in a straight line, place one forearm against the edge of your desk or the seat of your chair\n'\
                '2. Raise the other arm towards the ceiling\n'\
                '3. Hold this position for at least 30 seconds, then repeat on the other side\n\n'\
                '\nMuscle groups worked: Shoulde and Core\n'),
                "img": {
                    "img1": "./Images/Plank1.jpg"
                    }
            },
        
    }


#----- function to show the exercise window -----#
def showWindow():
    imageLabel.destroy()
    window.deiconify()
 
#----- function to hide the exercise window and restart timer to 30secs -----#
def hideWindow():
    imageLabel.destroy()
    window.withdraw()
    countdown(int(30))
    
#----- function to stop mainloop and closes the exercise window -----#
def closeWindow():
    window.quit()
    window.destroy()
    
#----- function to displayExercisePanel() ------#
def displayExercisePanel():
        
        #show the exercise frame to clean up previous images
        showWindow()       
            
        #generate random number to show random exercise
        rand = random.randint(0,9)
        print("Random#:", rand)

        #pass the random number to show the nth message by iterating through dictionary
        iterateDict(list(exerciseDetails.items())[rand][1],window,0)
        
        #initialise counter for image label array
        cnt = 0
        
        #show the associated images from the image list
        for path in imgList:
            #check if the path has .jpg file
            if path.find('jpg') != -1:
                
                #create tkinter image 
                img = ImageTk.PhotoImage(file=path)
                
                imageLabel = Label(window, image=img, width='400', height='450')
                imageLabel.grid(row=1, column=cnt, columnspan=2, padx=5, pady=5)
                
                cnt += 1
            
        
        #remind later button
        reminderBtn = Button(
                window,
                text = ' Thanks! Remind me again!! ',
                padx=5,
                pady=5,
                bg='#3299a8',
                fg='#ffffff',
                command = hideWindow)
        reminderBtn['font'] = btnFont
        reminderBtn.grid(row=2, column=0, padx=20, pady=10)

        #cancel button
        cancelBtn = Button(
                window,
                text = ' No thanks! Don\'t remind me ',
                padx=5,
                pady=5,
                bg='#a84032',
                fg='#ffffff',
                command = closeWindow)
        cancelBtn['font'] = btnFont
        cancelBtn.grid(row=2, column=1, padx=20, pady=10)
        window.mainloop()
#----- end of function displayExercisePanel() -----#


#invoke the countdown function for timer, pass the time interval as 30 secs
countdown(int(30))

#----end of main -----#

