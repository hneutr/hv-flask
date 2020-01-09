title: The Case for Groups
tags: [organization]
date: 2014-09-08

I’m not satisfied with my computer’s file system organization. 

Right now there are two independent (but overlapping) ways to organize content:

1. Folders
2. Tags

I don’t think either of these options is good enough, so I propose a hybrid type: the _group_. But first, why aren’t the traditional methods good enough?

---

Let’s look at folders. 

The concept behind the folder is old, predating computers by a _long_ time. 

A folder is: an object with a name containing other objects, which can be files or other folders.

---

What information do folders convey, and how can they be interacted with?

- A folder’s name describes the objects it contains. 
    - A folder’s name defines a space for the objects in it, and if an object in that folder is not contained in that space, it is in the wrong place. (e.g. if a folder is named ‘Music’, anything in that folder that is _not_ music is mislabeled)
- A set of folders is hierarchal in structure. 
    - Folders not contained by any other folder are at the top level, and any folder contained by _n_ other folders exists at level _n_. If I want to get to a folder a level _n_, I have to go through the other (_n_ - 1) folders. 
- A folder—and anything in it—exists in a single location. 
    - This follows from their hierarchal organization and historically physical character: a folder is modeled after a physical thing, so it "can’t" exist in two places at once. 

Folders are great for organizing physical objects in the physical world, but I don’t think they are the optimal solution for digital objects in the digital world. Digital objects don’t need to obey all properties of the physical world (though I am certainly _not_ saying they can be caused by anything outside it). Limiting their organization to what can be done in the physical world doesn't make much sense.

---

What are the problems with folders?

1. There are times when an object nested in some number of folders doesn’t fit exclusively under its label. 
    - Imagine a folder labeled ‘Music’, containing, surprisingly, a bunch of music, and also several music reviews. Those reviews _aren’t_ music, but they are _definitely_ associated. The reviews and the music files could each have their own folder, and be inside a containing ‘Related to Music’ folder, but I find this solution a tad unattractive.
2. There are times when it is problematic for a folder to exist in a rigid hierarchy. 
    - Let’s say you have a deeply nested folder, but that folder is also one you access frequently. It _does_ fit its label, deep within its folder structure, but it’s inconvenient to have it so far from reach. Putting it in a more prime location solves the ease of access issue, but at the cost of valuable (and pertinent) information.
3. There are times when a file or folder should exist in more than one location. 
    - Imagine two folders, ‘Work’ and ‘Videos’ and a video file that is associated with Work. Should it be in the Work folder or the Videos folder?

---

Tags solve many of the problems with folders, so let’s pause to take a look at tags.

A tag is: an adjective which can be attached to an object.

What information do tags convey, and how can they be interacted with?

- Like a folder, a tag’s name describes the objects it is attached to. 
- A tag has an associated ’tag-folder’, containing all the objects with that tag. 
    - This 'tag-folder’ exists in a single location (the tag-list), and anything with that tag has a reference to that location.
- Tags are not hierarchal, and multiple tags can be attached to an object.
- A tagged object must exist within a folder.

It isn’t possible to organize things by tag in the real world: you can’t physically gather together all the ‘fast things’ that exist, but virtually, a computer can. Tags are powerful, and aren’t limited by most of the constraints of folders, but this freedom comes with its own limitations. 

---

What problems do tags solve?

Well, they solve all the problems with folders:

1. An object always fits under its tags, since tags are actively added.
2. A tag is not bound to a hierarchal system, and can be accessed by the tag list or by a tagged object. 
3. An object in any location (folder) can be tagged with any tag.

---

So what are the problems with tags?

1. There are times when it would be desirable to have a tag-folder exist in a location other than the tag-list. 
    - I might want to access everything I’ve tagged as 'To Do’ from my desktop, without searching through the tag-list.
2. There are times when a tag should exist within a hierarchal organization. 
    - Suppose I have two tags, a ‘dark roast’ tag and a ‘light roast’ tag, and that everything tagged with either of these two tags also has a ‘coffee’ tag. Because 'dark roast' and 'light roast' only exist within the context of the 'coffee' tag, they are _dependent_ on the coffee tag - they function as a tag (adjective) for a tag. 
3. There are times when a tagged object shouldn’t be in a folder. 
    - There is no reason to force an object to exist in a folder. 

---

Tags and Folders each provide functionality the other lacks, but there are issues with both.

I propose a different organizational unit which subsumes both tags and folders: the _group_. 

A group is like a circle in a venn-diagram.

1. an object can be a part of one or more groups.
2. a group can contain other group-folders or objects.
    - If a group is contained entirely within another group, it is _dependent_ on that group.
3. a group exists in the group-list if it is not dependent, and within its dependent group's group-list if it is dependent.
4. a group, or the intersection of several groups, can exist as a group-folder object within another group. (e.g. a group-folder containing the intersection of the groups ‘Schoolwork’, ‘Current’, and ‘Algorithms’ could be placed on the desktop)

Folders would become group-folders but otherwise function normally. 

A file created in a group-folder would be automatically added to that group (or groups), but could also be added to a different group, set of groups, or group-folder.

A group could be ‘detached’ from its location, leaving it ‘attached’ only to the group-list. 

---

Which organizational problems confronting folders and tags do groups solve?

Looking at (my) list of the problems facing tags and folders, they address each.

For folders:

1. Objects in groups aren’t nested, and are rather referenced in only the groups which they are assigned to. Group-folders and group-folders within groups work like intersecting sets, so only the objects in both group 1 _and_ 2 are shown if group 2 is a group-folder within group 1 or if both form a group-folder.
2. Groups are not rigidly hierarchal, and can exist in more than one location.
3. Objects can exist in more than one group, and can be referenced in more than one location. 

For tags: 

1. A group can exist as a group-folder within another group or as a group-folder itself, and aren’t restricted to the group-list.
2. Organization of dependent groups makes hierarchal structure of groups possible.
3. An item in a group that is not a group-folder or contained within a group-folder can be accessed only from within the group-list.

---

Groups solve all the issues I have with the tag-folder system. 

I think it would be a better way of organizing.
