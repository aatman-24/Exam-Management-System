from copy import deepcopy
base = {
    "font_name" : "Calibri",
    "border" : True,
    "font_color" : "black",
    "pattern" : 1,
    "valign" : "vcenter",
    "font_size" : 14,
    "align" : "left",
    "locked" : True,
}

do_not_modify = deepcopy(base)
do_not_modify.update({
    "font_size" : 16,
    "bg_color" : "#C5D9F1",
    "font_color" : "#736532",
    "align" : "center",
    "bold" : True,

})
    
exam_detail = deepcopy(base)
exam_detail.update({
    "font_size" : 20,
    "bg_color" : "#C6E0B4",
    "align" : "center",
    "bold" : True,
})

exam_sub_details = deepcopy(base)
exam_sub_details.update({
    "font_size" : 14,
    "font_color" : "black",
    "bg_color" : "#C6E0B4",
    "align" : "left", 
    "bold" : True,
})

exam_sub_details_ans = deepcopy(base)
exam_sub_details_ans.update({
    "bg_color" : "white",
    "font_size" : 14,
    "font_color" : "black",
    "align" : "left", 
    "bg_color" : "#D6DCE4",
})


absent = deepcopy(base)
absent.update({
    "font_size" : 14,
    "bg_color" : "#C6E0B4",
    "align" : "center",
    "bold" : True,
})
   
AB = deepcopy(base)  
AB.update({
    "bg_color" : "white",
    "font_size" : 14,
    "align" : "center",
    "bold" : True,
})

roll_number_header = deepcopy(base)
roll_number_header.update({
    "bg_color" : "#C6E0B4",
    "align" : "center",
    "bold" : True, 
})

roll_number_format = deepcopy(base) 
roll_number_format.update({
    "bg_color" : "#C6E0B4",
    "align" : "left", 
    "font_size" : 11,
    "bold" : True,
})


marks = deepcopy(base)
marks.update({
    "bg_color" : "#D6DCE4",
    "align" : "left", 
    "font_size" : 11,
    "bold" : False,
    "locked" : False,
})

mark_header = deepcopy(base)
mark_header.update({
    "bg_color" : "#D6DCE4",
    "align" : "center", 
    "bold" : True,
})
