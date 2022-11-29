export START_DIR=$PWD
export HNEGOLF_DIR=/Users/hne/Documents/projects/hnegolf
export HNEGOLF_BUILD_DIR=$HNEGOLF_DIR/build
export HNEGOLF_CV_PATH=$HNEGOLF_DIR/templates/cv.html

export RESUMATOR_DIR=/Users/hne/Documents/projects/resumator
export RESUMATOR_CV_PATH=$RESUMATOR_DIR/generated.html

# generate the cv
cd $RESUMATOR_DIR
python run.py
cp $RESUMATOR_CV_PATH $HNEGOLF_CV_PATH

# build the site
cd $HNEGOLF_DIR
python run.py --build

# commit the changes
cd $HNEGOLF_BUILD_DIR
gptd

cd $PWD
# git add .
# export COMMIT_MESSAGE_DATE_STRING=$(date)
# git commit -m "$COMMIT_MESSAGE_DATE_STRING - site update"
# git push
# cd ..
