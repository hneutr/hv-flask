export START_DIR=$PWD

export GOLF_ROOT=$HOME/lib/golf
export GOLF_BUILD_DIR=$GOLF_ROOT/.build
export GOLF_CV_PATH=$GOLF_ROOT/templates/cv.html

export RESUMATOR_DIR=/Users/hne/Documents/projects/resumator
export RESUMATOR_CV_PATH=$RESUMATOR_DIR/generated.html

# generate the cv
cd $RESUMATOR_DIR
python run.py
cp $RESUMATOR_CV_PATH $GOLF_CV_PATH

# build the site
cd $GOLF_ROOT
python run.py --build

# commit the changes
cd $GOLF_BUILD_DIR
git add .
export COMMIT_MESSAGE_DATE_STRING=$(date)
git commit -m "$COMMIT_MESSAGE_DATE_STRING update"
git push

cd $START_DIR
