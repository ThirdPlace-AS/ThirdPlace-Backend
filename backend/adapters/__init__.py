"""External provider adapters (Supabase, Celery/Redis).

Adapters isolate third-party SDKs behind our own boundary so domain/repository
code never imports vendor clients directly. Phase 0 wires the boundaries but
contacts nothing.
"""
