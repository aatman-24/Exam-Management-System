STUDENT :
    student/create
    student/<slug:student_slug>/
    student/<slug:student_slug>/update
    student/<slug:student_slug>/delete
    student/list/?order_by=rollNumber&&limit=5&&div=a&&std=11
    student/profile
    student/parent-profile

PROFILE:
    profile/<slug:student_slug>/create
    profile/<slug:student_profile_slug>/
    profile/<slug:student_profile_slug>/update
    profile/<slug:student_profile_slug>/delete

PARENT_PROFILE:
    parent-profile/<slug:student_slug>/create
    parent-profile/<slug:parent_profile_slug>
    parent-profile/<slug:parent_profile_slug>/update/
    parent-profile/<slug:parent_profile_slug>/delete/







http://example.com/api/products/4675/?category=clothing&max_price=10.00