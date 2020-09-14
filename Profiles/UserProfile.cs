using AutoMapper;
using JoinClub.Entities.Application;
using JoinClub.Models.Account;
using JoinClub.Models.User;

namespace JoinClub.Profiles
{
    public class UserProfile : Profile
    {
        public UserProfile()
        {
            // RegisterViewModel 傳換成 ApplicationUser
            CreateMap<RegisterViewModel, ApplicationUser>()
                .ForMember(dest => dest.Email,
                    opt => opt.MapFrom(src => src.Email))
                .ForMember(dest => dest.UserName,
                    opt => opt.MapFrom(src => src.UserName))
                .ForMember(dest => dest.PhoneNumber,
                    opt => opt.MapFrom(src => src.PhoneNumber))
                .ForMember(dest => dest.NID,
                    opt => opt.MapFrom(src => src.NID))
                .ForMember(dest => dest.Name,
                    opt => opt.MapFrom(src => src.Name))
                .ForMember(dest => dest.College,
                    opt => opt.MapFrom(src => src.College))
                .ForMember(dest => dest.Department,
                    opt => opt.MapFrom(src => src.Department))
                .ForMember(dest => dest.Class,
                    opt => opt.MapFrom(src => src.Class));

            // ApplicationUser 傳換成 UserViewModel
            CreateMap<ApplicationUser, UserViewModel>()
                .ForMember(dest => dest.Id,
                    opt => opt.MapFrom(src => src.Id))
                .ForMember(dest => dest.Email,
                    opt => opt.MapFrom(src => src.Email))
                .ForMember(dest => dest.UserName,
                    opt => opt.MapFrom(src => src.UserName))
                .ForMember(dest => dest.PhoneNumber,
                    opt => opt.MapFrom(src => src.PhoneNumber))
                .ForMember(dest => dest.NID,
                    opt => opt.MapFrom(src => src.NID))
                .ForMember(dest => dest.Name,
                    opt => opt.MapFrom(src => src.Name))
                .ForMember(dest => dest.College,
                    opt => opt.MapFrom(src => src.College))
                .ForMember(dest => dest.Department,
                    opt => opt.MapFrom(src => src.Department))
                .ForMember(dest => dest.Class,
                    opt => opt.MapFrom(src => src.Class));
        }
    }
}