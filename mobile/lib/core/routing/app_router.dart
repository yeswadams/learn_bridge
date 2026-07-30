import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

import '../../features/splash/presentation/splash_screen.dart';
import '../../features/onboarding/presentation/screens/onboarding_screen.dart';
import '../../features/auth/presentation/screens/login_screen.dart';
import '../../features/calendar/presentation/calendar_screen.dart';
import '../../features/courses/presentation/screens/courses_list_screen.dart';
import '../../features/courses/presentation/screens/course_details_screen.dart';
import '../../features/courses/presentation/screens/lesson_player_screen.dart';
import '../../features/dock/presentation/dock_shell.dart';
import '../../features/home/presentation/home_screen.dart';
import '../../features/profile/presentation/screens/profile_screen.dart';

final GoRouter appRouter = GoRouter(
  initialLocation: '/splash',
  routes: [
    GoRoute(
      path: '/splash', 
      builder: (context, state) => const SplashScreen(),
    ),
    GoRoute(
      path: '/onboarding', 
      builder: (context, state) => const OnboardingScreen(),
    ),
    // App dock routes
    StatefulShellRoute.indexedStack(
      builder: (context, state, navigationShell) {
        return DockShell(navigationShell: navigationShell);
      },
      branches: [
        // Home Page
        StatefulShellBranch(
          routes: [
            GoRoute(path: '/home',
            builder: (context, state) => const HomePage(),
            ),
          ],
        ),
        // Calendar
        StatefulShellBranch(
          routes: [
            GoRoute(
              path: '/calendar',
              builder: (context, state) => const CalendarPage(),
            ),
          ],
        ),
        // Courses List
        StatefulShellBranch(
          routes: [
            GoRoute(
              path: '/courses-list',
              builder: (context, state) => const CoursesListPage(),
            ),
          ],
        ),
        // Courses Details Page
        StatefulShellBranch(
          routes: [
            GoRoute(
              path: "/courses-details",
              builder: (context, state) => const CourseDetailsPage(),
            ),
          ],
        ),
        // Lesson player
        StatefulShellBranch(
          routes: [
            GoRoute(
              path: '/lesson-player',
              builder: (context, state) => const LessonPlayerPage(),
            ),
          ],
        ),
        //  Profile Page
        StatefulShellBranch(
          routes: [
            GoRoute(
              path: '/profile',
              builder: (context, state) => const ProfilePage(),
            ),
          ],
        ),
      ] 
    )
  ],
);
