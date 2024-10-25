import db

db.update("td_tasks", {
    "title": "TEST",
    "summary": "Summary Test"
}, {
    "id" : "1"
})