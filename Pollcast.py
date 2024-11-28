import streamlit as st

# Poll options and vote storage
poll_options = {'Option 1': 0,'Option 2': 0, 'Option 3': 0,'Option 4': 0}
poll=poll_options.items()

# Function to save poll results to a file
def save_results():
    try:
        with open("poll_results.txt", "w") as obj1:
            for option,votes in poll: #unpack
                obj1.write(f"{option}: {votes} votes\n")
    except Exception as e:
        st.error(f"Error saving results: {e}")

# Function to load poll results from a file
def load_results():
    try:
        with open("poll_results.txt", "r") as obj2:
            lines = obj2.readlines() # ["Option 1: 0 votes\n" ,"Option 2: 0 votes\n"," Option 3: 0 votes\n"," Option 4: 0\n"]
            for i in lines:
                options,votes = i.strip().split(': ')
                poll_options[options] = int(votes.split()[0])
    except FileNotFoundError:
        pass  # If file doesn't exist, continue with default values
    except Exception as e:
        st.error(f"Error loading results: {e}")

# Function to reset poll results
def reset_results():
    for i in poll_options.keys():
        poll_options[i] = 0
    save_results()  # Save reset results to file

# Main function for the Polling App
def main():
    st.title("PollCast")
    st.markdown("### Vote for Your Favorite Option")

    # Load results if available
    load_results()

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select a page", ("Vote", "Results"))

    # Buttons for refresh and reset
    st.sidebar.button("Refresh Results", on_click=load_results)
    if st.sidebar.button("Reset Poll"):
        reset_results()
        st.success("Poll has been reset.")

    if page == "Vote":
        # Radio button to choose the poll option
        vote = st.radio("Choose an option:", list(poll_options.keys()))

        # Button to submit the vote
        if st.button("Vote"):
            poll_options[vote] += 1
            st.success(f"You voted for: {vote}")
            save_results()  # Save results after voting

    elif page == "Results":
        # Display the current poll results
        st.subheader("Current Poll Results:")
        for option, votes in poll_options.items():
            st.write(f"{option}: {votes} votes")

        # Display the results as a bar chart
        st.bar_chart(poll_options)

    # Additional information
    st.markdown("### Thank you for participating!")

if __name__ == "__main__":
    main()
