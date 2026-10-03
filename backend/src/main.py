from fastapi import FastAPI
from src.middlewares.auth_middleware import auth_middleware
from src.middlewares.audit_log_middleware import audit_log_middleware
from src.routes.track_section_routes import router as track_section_router
from src.routes.track_defect_routes import router as track_defect_router
from src.routes.work_window_routes import router as work_window_router
from src.routes.rectification_task_routes import router as rectification_task_router
from src.routes.review_record_routes import router as review_record_router

app = FastAPI(title="铁路工务病害整治系统")
app.middleware("http")(auth_middleware)
app.middleware("http")(audit_log_middleware)

@app.get("/health")
def health():
    return {"status": "ok", "service": "rail-defect"}

app.include_router(track_section_router)
app.include_router(track_defect_router)
app.include_router(work_window_router)
app.include_router(rectification_task_router)
app.include_router(review_record_router)
