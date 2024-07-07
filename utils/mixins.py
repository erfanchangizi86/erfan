from django.core.cache import cache


class CacheListViewMixin:
    cache_timeout = 300  # زمان اعتبار کش به ثانیه

    def get_cache_key(self):
        # تولید کلید کش بر اساس نام کلاس و پارامترهای ورودی مانند مسیر درخواست و پارامترهای موجودیت
        return f'{self.__class__.__name__}_cache_{self.request.path}'

    def cache_get_or_set(self, view_func):
        def wrapped_view(*args, **kwargs):
            cache_key = self.get_cache_key()
            cached_data = cache.get(cache_key)
            if cached_data:
                return cached_data

            # اگر داده در کش نبود، لیست موجودیت‌ها را دریافت می‌کنیم
            queryset = view_func(*args, **kwargs)
            cached_data = list(queryset)
            cache.set(cache_key, cached_data, timeout=self.cache_timeout)

            return cached_data

        return wrapped_view