# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)














#INPUT (Dashboard)


    {
        from: "Fri Dec 09 2022 17:17:43 GMT+0530",
        to: "Sat Dec 10 2022 14:16:40 GMT+0530"
    }


#OUTPUT (Dashboard)

[
    {
        cycle_id: "139182bs8d",
        cycle_name: "any random name",
        tasks: {
            task1: "2.3",
            task2: "8.9",
            task3: "6.4"
        }
    },
    {
        cycle_id: "y23v23784v",
        cycle_name: "any other random name",
        tasks: {
            task1: "7.3",
            task2: "4.8",
            task3: "9.2"
        }
    },
    {
        cycle_id: "8awfba8fbd",
        cycle_name: "any random name",
        tasks: {
            task1: "5.2",
            task2: "7.1",
            task3: "8.7"
        }
    }
]

#Getting the last 10 cycles every 5-10 seconds to check for new data in the Live Feed

[
    {
        video: {
            video_id: "344hn24f",
            video_src: "http:sdasd/video.mp4"
        }
        tasks: [
            {
                task_no: "1",
                task_name: "Engine Assembly",
                time_taken: "11 sec",
                status: "on time"
            },
            {
                task_no: "2",
                task_name: "Tyre Assembly",
                time_taken: "18 sec",
                status: "on time"
            },
            {
                task_no: "3",
                task_name: "Gearbox Testing",
                time_taken: "12 sec",
                status: "on time"
            }
        ]
    },
        {
        video: {
            video_id: "23794b2b",
            video_src: "http:sdasd/video.mp4"
        }
        tasks: [
            {
                task_no: "1",
                task_name: "Engine Assembly",
                time_taken: "23 sec",
                status: "late"
            },
            {
                task_no: "2",
                task_name: "Tyre Assembly",
                time_taken: "12 sec",
                status: "on time"
            },
            {
                task_no: "3",
                task_name: "Gearbox Testing",
                time_taken: "16 sec",
                status: "on time"
            }
        ]
    },
    ...
]