namespace JoinClub.Helpers
{
    public class UserResourceParameters
    {
        // 最大一次返回的項目數量
        private const int MaxPageSize = 50;

        // 預設一次返回的項目數量
        private int _pageSize = 10;

        // 目前頁數，預設 1
        public int PageNumber { get; set; } = 1;

        public int PageSize
        {
            get => _pageSize;
            set => _pageSize = (value > MaxPageSize) ? MaxPageSize : value;
        }
    }
}