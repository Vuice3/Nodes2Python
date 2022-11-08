-Guide & Documentation for Nodes2Python-


HOW TO USE :

Start by putting the stickfigure you wish to convert in the same directory as 'nodes2python.py' . Then rename the stickfigure file to "input.nodes" .

After that, all you need to do is open 'nodes2python.py' with your python interpreter. After it finishes running, wait a few moments and a file called 'output.py' should appear in the same directory. This is your outputted file and you can use it in any way you wish.

(It's important to note that you should move input.nodes and output.nodes out of the directory immediately after the conversion, so you don't accidentally run the program again and cause errors.)


DOCUMENTATION :

---
(NOTE - I highly reccomend you go read the documentation on the node format made by Vince the Animator (@vincetheanimator at sticknodes.com). Here's a mirror download link to that: https://cdn.discordapp.com/attachments/854456068196007958/1036820814143696967/NODES_FORMAT_334.txt
---

This will go over how to read the dictionary in the outputted file.

- Directory system :
The outputted file uses a dictionary, with the key for each object being decided by a 'directory system' of sorts.
To provide an example - To call the "Is Stretchy" boolean for the node with ID 26, you would do something like this:
```
stickfigureData['node_26_IsStretchy']
```

Or if you wanted to call the stickfigure color's alpha, you would do:
```
stickfigureData['alpha']
```
This directory system of sorts will make it much easier to specify what data you exactly want from the dictionary, since it's in a very human-readable format compared to the actual .nodes format .

Now that we got the basics out of the way, it's time to look at what can actually be inside this directory. Starting with..

- 'ver' :

You saw this earlier, but this is just the sticknodes version number. It comes in handy when creating backwards-compatibility for older versions of sticknodes. This is always an integer between 0 to latest version (Currently 334 as of writing this).

- 'scale' :

The stickfigure scale represented as a floating-point.

- 'alpha' :

The stickfigure color's alpha as an integer, range 0-255

- 'blue' :

The stickfigure color's blue amount as an integer, range 0-255

- 'green' :

The stickfigure color's green amount as an integer, range 0-255

- 'red' :

The stickfigure color's red amount as an integer, range 0-255


- 'nodeCount' :

The amount of nodes in the stickfigure, excluding the main node (int)


- 'node_x_y' :

(x = the node's ID, y = the property of that node)

Narrows down the directory to the node ID and the property of that node.
Ex:
```
stickfigureData[node_1_Scale] # << Get the segment scale for the node with ID 1.
```

- 'node_x_Type' :

The type of limb that the node with ID 'x' has. (integer, range -1 to 7)
       -1 = main node
	0 = rounded segment
	1 = segment
	2 = circle
	3 = triangle
	4 = outlined circle (A.K.A. filled circle)
	5 = ellipse
	6 = trapezoid
	7 = polygon
(polyfills are not determined by node_x_Type.)


- 'node_x_Layer' :

The draw order for node 'x' . Also acts as the node ID, only one node can be on a single layer at once. The draw order for the main node is always 0.

- 'node_x_IsStatic' :

The "Is Static?" boolean for node 'x' .

- 'node_x_IsStretchy' :

The "Is Stretchy?" boolean node 'x' .

- 'node_x_IsSmartStretch' :

The "Is Smart Stretch?" boolean for node 'x' . Only on versions 248 and greater.

- 'node_x_DontSmartStretch' :

The "Do Not Apply Smart Stretch" boolean for node 'x' . Only on versions 252 and greater.

- 'node_x_UseSegmentColor' :

The "Use Segment Color" boolean for node 'x' .

- 'node_x_UseCircleOutline' :

The "Use Circle Outline" boolean for node 'x' . Only on versions 256 and greater.

- 'node_x_UseGradientColor' :

The "Use Gradient" boolean for node 'x' . Only on versions 176 and greater.

- 'node_x_ReverseGradient' :

The "Reverse Gradient?" boolean for node 'x' . Only on versions 176 and greater.

- 'node_x_UseSegmentScale : 

The "Use Segment Scale" boolean for node 'x' .

- 'node_x_LocalX' :

The X offset from the parent node for node 'x' . I don't know much about this so I cant document it well, but a positive float = rightward direction , negative float = leftward direction. You probably wont need this if you have the angle and length already, the creator of Sticknodes said this was just for optimization purposes.

- 'node_x_LocalY' :

The Y offset from the parent node for node 'x' . I don't know much about this so I cant document it well, but a positive float = upward direction , negative float = downward direction. You probably wont need this if you have the angle and length already, the creator of Sticknodes said this was just for optimization purposes.

- 'node_x_Scale' : 

The segment scale for node 'x' . (floating-point)

- 'node_x_DefaultLength' : 

The default length for node 'x' . In most cases this is just the same as node_x_Length. (floating-point)

- 'node_x_Length' : 

The length for node 'x' . (floating-point)

- 'node_x_DefaultThickness' :

The default thickness for node 'x' . In most cases this is just the same as node_x_Thickness. (integer)

- 'node_x_Thickness' :

The thickness for node 'x' . (integer)

- 'node_x_SegmentCurveRadius' :

The curve radius for a segment. Only on versions 320 and greater.

- 'node_x_IsHalfArc' :

The "Is half arc?" boolean for node 'x' . Only on versions 256 and greater.

- 'node_x_RightTriangleDirection' :

The right triangle direction for node 'x' . Only on versions 256 and greater. (integer)

- 'node_x_TriangleUpsideDown' :

The boolean that flips the triangle upside down for node 'x' . Only on versions 300 and greater. (floating-point)

- 'node_x_TrapezoidTopThicknessRatio' :

The ratio for the thickness of the top of the trapezoid for node 'x' . Only on versions 256 and greater. (floating-point)

- 'node_x_NumberOfPolygonVertices' :

The number of polygon vertices for node 'x' . (integer)

- 'node_x_DefaultLocalAngle' :

This is normally the same as node_x_LocalAngle, but I don't know much about it. Only on versions 248 and greater. (floating-point)

- 'node_x_LocalAngle' :

The Local Angle for node 'x' . I don't know much about localAngle, once again ask the creator of Sticknodes for more info on these things. (floating-point)

- 'node_x_DefaultAngle' :

The default angle for node 'x' . Only on versions 248 and greater. (floating-point)


- 'node_x_SegmentColor_Alpha' :

The alpha for node 'x' segment color. (int, range 0-255)

- 'node_x_SegmentColor_Blue' :

The blue amount for node 'x' segment color. (int, range 0-255)

- 'node_x_SegmentColor_Green' :

The green amount for node 'x' segment color. (int, range 0-255)

- 'node_x_SegmentColor_Red' :

The red amount for node 'x' segment color. (int, range 0-255)

- 'node_x_GradientColor_Alpha' :

The alpha for node 'x' gradient color. Only on version 176 and greater. (int, range 0-255)

- 'node_x_GradientColor_Blue' :

The blue amount for node 'x' gradient color. Only on version 176 and greater. (int, range 0-255)

- 'node_x_GradientColor_Green' :

The green amount for node 'x' gradient color. Only on version 176 and greater. (int, range 0-255)

- 'node_x_GradientColor_Red' :

The red amount for node 'x' gradient color. Only on version 176 and greater. (int, range 0-255)

- 'node_x_CircleOutlineColor_Alpha' :

The alpha for node 'x' circle outline color. Only on version 256 and greater. (int, range 0-255)

- 'node_x_CircleOutlineColor_Blue' :

The blue amount for node 'x' circle outline color. Only on version 256 and greater. (int, range 0-255)

- 'node_x_CircleOutlineColor_Green' :

The green amount for node 'x' circle outline color. Only on version 256 and greater. (int, range 0-255)

- 'node_x_CircleOutlineColor_Red' :

The red amount for node 'x' circle outline color. Only on version 256 and greater. (int, range 0-255)

- 'node_x_NumberOfChildNodes' :

The amount of child nodes that node 'x' has. (integer)

- 'node_x_Parent' :

The ID of the parent node for node 'x' . Not part of the actual sticknodes file format, but this is added ontop due to python dictionary limitations. Use this to deter between parent, child, and sister nodes. (int)

----    								             ----
!!!!!(BELOW IS ALL POLYFILL DIRECTORIES. THEY ARE ONLY ON VERSION IS 230 OR GREATER)!!!!!
----      						        		     ----


- 'polyfill_x_y' :

Narrows down the directory to the anchor node's ID and the property of that polyfill.

- 'numberOfPolyfills' :

The amount of polyfills that are in the stickfigure. Not to be confused with the number of connections a polyfill has. (integer)

- 'polyfill_x_ParentNode' :

The ID of the anchor node for the polyfill. (int)

- 'polyfill_x_Color_Alpha' :

The alpha for polyfill 'x' . (int, range 0-255)

- 'polyfill_x_Color_Blue' :

The blue amount for polyfill 'x' . (int, range 0-255)

- 'polyfill_x_Color_Green' :

The green amount for polyfill 'x' . (int, range 0-255)

- 'polyfill_x_Color_Red' :

The red amount for polyfill 'x' . (int, range 0-255)

- 'polyfill_x_UsePolyfillColor' :

The "Use Polyfill color" boolean for polyfill 'x' .

- 'polyfill_x_NumberOfPolyfillNodes'

The amount of connections a polyfill has, excluding the anchor node.

- 'polyfill_x_Connection_y_Layer' :

(replace "y" with the chronological order number of the connection. 0 being first, 1 being second, etc.)
The ID of the node the 'y'th connection of polyfill 'x' is. Example:
```
stickfigureData[polyfill_2_Connection_0] # << The directory for the node ID of Polyfill 2's first connection.
```

-----------------

End of documentation. If you have any questions, ping @dubsyne at sticknodes.com,
or DM Dubstyne#1104 on discord.


